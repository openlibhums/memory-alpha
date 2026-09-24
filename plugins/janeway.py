from datetime import datetime
import logging
import os
import re
from tempfile import NamedTemporaryFile
from urllib.request import pathname2url

from jinja2 import ChoiceLoader, Environment, FileSystemLoader

from pelican import contents, signals, DEFAULT_CONFIG_NAME
from pelican.readers import HTMLReader, BaseReader
from pelican.settings import read_settings
from pelican.utils import pelican_open
from marko import Markdown
from marko.ast_renderer import ASTRenderer
from marko.ext.gfm import GFM
from marko.helpers import MarkoExtension
from marko.ext.toc import slugify


log = logging.getLogger(__name__)


SETTINGS = read_settings(DEFAULT_CONFIG_NAME)


def load_jinja_environment(settings):

    # This function is partially adapted from the pelican-jinja2content plugin.
    # We copy and adapt it rather than using it
    # so that we can use Marko for Markdown processing.
    # https://github.com/pelican-plugins/jinja2content

    content_dir = settings["PATH"]
    theme_dir = os.path.join(settings["THEME"], "templates")
    loaders = [
        FileSystemLoader(_dir) for _dir in [content_dir, theme_dir]
    ]

    jinja_environment_settings = settings["JINJA_ENVIRONMENT"]
    environment = Environment(
        loader=ChoiceLoader(loaders),
        **jinja_environment_settings
    )
    if "JINJA_FILTERS" in settings:
        environment.filters.update(settings["JINJA_FILTERS"])
    if "JINJA_GLOBALS" in settings:
        environment.globals.update(settings["JINJA_GLOBALS"])
    if "JINJA_TEST" in settings:
        environment.tests.update(settings["JINJA_TESTS"])
    return environment


JINJA_ENV = load_jinja_environment(SETTINGS)

MD_FILE_ENDING_RE = re.compile(r"\.md$")
MD_FILE_ENDING_FRAGMENT_RE = re.compile(r"\.md\#")


class JanewayRendererMixin:
    # This is a Marko mixin
    # https://marko-py.readthedocs.io/en/latest/extend.html#create-an-extension-object

    def render_heading(self, element):
        # From overwritten function
        children = self.render_children(element)
        level = element.level
        if level > 1:
            section_id = slugify(JINJA_ENV.filters["striptags"](children))
        else:
            section_id = ""

        # New behaviour
        context = {
            "level": level,
            "children": children,
            "section_id": section_id,
        }
        template = JINJA_ENV.get_template("components/rendered_heading.html")
        return template.render(context)

    def render_alert(self, element):
        # From overwritten function
        header = self.escape_html(element.alert_type)
        children = self.render_children(element)

        # New behavior
        alert_type = element.alert_type.lower()
        if alert_type == "note":
            icon = "info-circle"
        elif alert_type == "tip":
            icon = "bulb"
        elif alert_type == "important":
            icon = "message-report"
        elif alert_type == "warning":
            icon = "alert-triangle"
        elif alert_type == "caution":
            icon = "alert-octagon"
        else:
            icon = "info-circle"
        context = {
            "alert_type": alert_type,
            "icon_file": f"svg/tabler/{ icon }.svg",
            "header_title": header.title(),
            "children": children,
        }
        template = JINJA_ENV.get_template("components/rendered_alert.html")
        return template.render(context)

    def render_link(self, element):
        # From overwritten function
        title = f' title="{self.escape_html(element.title)}"' if element.title else ""
        url = self.escape_url(element.dest)
        body = self.render_children(element)

        # New behavior
        url = re.sub(MD_FILE_ENDING_RE, "", url)
        url = re.sub(MD_FILE_ENDING_FRAGMENT_RE, "#", url)
        context = {
            "title": title,
            "url": url,
            "body": body,
        }
        template = JINJA_ENV.get_template("components/rendered_link.html")
        return template.render(context)


JanewayMarkoExtension = MarkoExtension(
    renderer_mixins=[JanewayRendererMixin],
)


class MarkoMarkdownReader(BaseReader):
    enabled = True
    file_extensions = ['md']

    def read(self, source_path):
        """Parse using Marko"""

        self._source_path = source_path
        markdown = Markdown(extensions=[GFM, JanewayMarkoExtension])
        ast = Markdown(extensions=[GFM, JanewayMarkoExtension], renderer=ASTRenderer)
        with pelican_open(source_path) as text:
            # Render to AST to pull some content out as metadata
            parsed_ast = ast(text)
            content = markdown(text)

        metadata = {}
        metadata["h2s"] = []
        for line in parsed_ast["children"]:
            if line["element"] == "heading":
                if line["level"] == 1:
                    # Use the h1 as the title
                    metadata["title"] = line["children"][0]["children"]
                elif line["level"] == 2:
                    # Collect the h2s
                    heading = line["children"][0]["children"]
                    section_id = slugify(JINJA_ENV.filters["striptags"](heading))
                    metadata["h2s"].append((heading, section_id))

        return content, metadata


class JinjaContentMixin:
    # This mixin is adapted from the pelican-jinja2content plugin.
    # We copy and adapt it rather than using it
    # so that we can use Marko for Markdown processing.
    # https://github.com/pelican-plugins/jinja2content

    def read(self, source_path):
        with pelican_open(source_path) as text:
            text = JINJA_ENV.from_string(text).render()

        with NamedTemporaryFile(delete=False) as f:
            f.write(text.encode())
            f.close()
            content, metadata = super().read(f.name)
            os.unlink(f.name)
            return content, metadata


class JinjaMarkdownReader(JinjaContentMixin, MarkoMarkdownReader):
    pass


class JinjaHTMLReader(JinjaContentMixin, HTMLReader):
    pass


def add_reader(readers):
    """Add Jinja readers."""
    for Reader in [JinjaMarkdownReader, JinjaHTMLReader]:
        for ext in Reader.file_extensions:
            readers.reader_classes[ext] = Reader


class AllSupportPagesGenerator:

    """
    Creates a comprehensive list of support pages.

    Adapted from the excellent Pelican sitemap plugin:
    https://github.com/pelican-plugins/sitemap/blob/main/pelican/plugins/sitemap/sitemap.py

    Note! We also *use* the sitemap plugin to generate a separate XML sitemap for indexers.
    """

    def __init__(self):
        """Initialize the generator."""
        self.now = datetime.now()
        self.page_queue = []
        self._main_pelican = None

    def init(self, pelican):
        """Initialize the all pages."""
        log.debug("AllSupportPagesGenerator: Initialize")
        if self._main_pelican is None:
            self._main_pelican = pelican

    def queue_page(self, path, context):
        """Queue one site page for later generation."""
        obj = context.get("article") or context.get("page")
        self.page_queue.append((path, obj))

    def finalize(self, pelican):
        """Write the output page using queued pages."""
        # Wait for all i18n_subsites to finish
        # https://github.com/pelican-plugins/sitemap/pull/3#discussion_r436390684
        if pelican == self._main_pelican:
            self._write_out(pelican)
            # Reset for autoreload
            self._main_pelican = None
            self.page_queue = []

    def _write_out(self, pelican):
        output_path = pelican.output_path
        log.debug("AllSupportPagesGenerator: Writing to %r", output_path)
        context = pelican.settings
        siteurl = context["SITEURL"]
        config = context.get("ALL_SUPPORT_PAGES", {})
        included = config.get("include", ())
        excluded = config.get("exclude", ())
        filename = os.path.join(output_path, "pages", "support", "all-support-pages.html")

        def to_url(path):
            nonlocal output_path
            return pathname2url(os.path.relpath(path, output_path))

        def is_included(item):
            nonlocal included
            url, obj = item
            return any(re.search(pattern, url) for pattern in included)

        def is_excluded(item):
            nonlocal excluded
            url, obj = item
            is_private = getattr(obj, "private", "") == "True"
            is_hidden = getattr(obj, "status", "published") != "published"
            return (
                is_private
                or is_hidden
                or any(re.search(pattern, url) for pattern in excluded)
            )

        # Use obj.url for articles/pages to respect custom URL settings
        # (e.g., ARTICLE_URL). Fall back to to_url(path) for index pages
        # (archives, tags, etc.) which don't have a .url property as they're
        # not Article or Page objects.
        page_queue = [
            (obj.url if obj else to_url(path), obj)
            for path, obj in self.page_queue
        ]
        page_queue = [
            page for page in page_queue if is_included(page) and not is_excluded(page)
        ]
        grouped_pages = {}
        for page_path, obj in page_queue:
            head, _tail = os.path.split(page_path)
            folder = head.split("/")[-1].replace("-", " ")
            if folder not in grouped_pages:
                grouped_pages[folder] = {
                    "index": None,
                    "pages": [],
                }
            page_dict = {
                "path": f"{siteurl}/{page_path}",
                "obj": obj
            }
            if page_path.endswith("index.html"):
                section_id = slugify(JINJA_ENV.filters["striptags"](obj.title))
                page_dict["section_id"] = section_id
                grouped_pages[folder]["index"] = page_dict
            else:
                grouped_pages[folder]["pages"].append(page_dict)

        # Sort on page title so pages in each section are alphabetical
        for key, folder in grouped_pages.items():
            sorted_pages = sorted(folder["pages"], key=lambda page: page["obj"].title)
            grouped_pages[key]["pages"] = sorted_pages

        # Convert to a tuple list to sort sections by index page title
        grouped_pages = list(grouped_pages.items())
        grouped_pages.sort(key=lambda group_tup: group_tup[1]["index"]["obj"].title)

        with open(filename, "w", encoding="utf-8") as fd:
            template = JINJA_ENV.get_template("all_support_pages.html")
            context["page"] = contents.Page(
                "",
                metadata={
                    "title": "All support pages",
                    "alpha_site": "support",
                }
            )
            context["output_file"] = "pages/support/all-support-pages.html"
            context["grouped_pages"] = grouped_pages

            fd.write(template.render(context))

        log.info(f"AllSupportPagesGenerator: Written {filename!r}")


generator = AllSupportPagesGenerator()


def register():
    """Register the plugin."""
    # Signals related to Markdown rendering
    signals.readers_init.connect(add_reader)

    # Signals related to "All Pages" page generation on support site
    signals.get_generators.connect(generator.init)
    signals.content_written.connect(generator.queue_page)
    signals.finalized.connect(generator.finalize)
