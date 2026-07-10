import os
from tempfile import NamedTemporaryFile

from jinja2 import ChoiceLoader, Environment, FileSystemLoader

from pelican import signals, DEFAULT_CONFIG_NAME
from pelican.readers import HTMLReader, BaseReader
from pelican.settings import read_settings
from pelican.utils import pelican_open
from marko import Markdown
from marko.ast_renderer import ASTRenderer
from marko.ext.gfm import GFM
from marko.helpers import MarkoExtension


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


class JanewayRendererMixin:
    # This is a Marko mixin
    # https://marko-py.readthedocs.io/en/latest/extend.html#create-an-extension-object

    pass


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
        # Use the h1 as the title
        for line in parsed_ast["children"]:
            if line["element"] == "heading" and line["level"] == 1:
                h1 = line["children"][0]["children"]
                metadata["title"] = h1
                break

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


def register():
    """Register the plugin."""
    signals.readers_init.connect(add_reader)
