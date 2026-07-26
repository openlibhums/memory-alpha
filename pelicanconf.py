from datetime import datetime
import json
import logging


TESTING = False
AUTHOR = 'Open Library of Humanities'
SITENAME = 'Janeway'
SITEURL = "http://localhost:8000" if TESTING else "https://janeway.systems"

PATH = "content"

TIMEZONE = 'Greenwich'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme
THEME = 'themes/alpha'
STYLESHEET_URL = 'theme/css/index.css'

# The following two lines tell Pelican to reproduce the exact structure
# of the content folder in the output folder (except for pages--specified below)
# We want this so that people can contribute content (including images)
# via the GitHub user interface, using the Preview tab in the markdown editor
# to check the content is rendering as expected.
PATH_METADATA = r'(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'

# Default metadata for all pages and articles
DEFAULT_METADATA = {
    # The default alpha_site is support so that we do
    # not have to specify it in every docs Markdown file.
    "alpha_site": "support",
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["janeway"]

# Custom settings used in tests/conftest.py
SUPPORT_CONTENT_PATH = "content/pages/support"

# Static
STATIC_PATHS = [
    'pages/support/images',
    'pages/support/downloadables',

    # Legacy paths from old docs
    # that we will eventually remove
    'old-docs/nstatic',
    'old-docs/nstatic/images',
    'old-docs/nstatic/image-guidelines',
    'old-docs/nstatic/typesetting',
    'old-docs/nstatic/typesetting/editor',
]

# Prevent HTML files in /static/components/ from being copied to served assets
IGNORE_FILES = [
    '**/components/*.html', # Currently not working due to Pelican bug
    # See https://github.com/getpelican/pelican/issues/1678#issuecomment-2376759249
]

# Nav
DISPLAY_PAGES_ON_MENU = False # We want to set the order manually
DISPLAY_CATEGORIES_ON_MENU = False
LEFT_NAV_ITEMS = [
    ('Our story', '/pages/our-story.html', ""),
    ('Hosting', '/pages/hosting.html', ""),
    ('Support', '/pages/support.html', ""),
]
RIGHT_NAV_ITEMS = [
    ('Symposium', 'https://thelowerdecks.janeway.systems/', "_blank"),
    ('Source code', 'https://github.com/openlibhums/janeway', "_blank"),
]
FOOTER_LINKS = [
    ('Accessibility', '/pages/accessibility-of-this-website.html', ""),
    ('Copyright', "/pages/copyright-and-licensing.html", ""),
    ('Open Library of Humanities', "https://www.openlibhums.org", "_blank"),

]
ALL_PAGES =  [
    ('Home', '/', ""),
] + LEFT_NAV_ITEMS + RIGHT_NAV_ITEMS + FOOTER_LINKS

# Use mtime of files as date in webpage metadata
DEFAULT_DATE = 'fs'

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.do'],
}

# Data for maps on Hosting page
INSTALLATION_GEOJSON = "themes/alpha/static/data/janeway_installations.geojson"
with open(INSTALLATION_GEOJSON) as ref:
    installation_json = ref.read()

JINJA_GLOBALS = {
    "current_year": datetime.now().strftime("%Y"),
    "installation_map_json": json.loads(installation_json),
}

# Filter out empty alt warnings, which do not account for the primary method of
# marking images as decorative, which is alt=""
LOG_FILTER = [(logging.WARN, 'Empty alt attribute for image %s in %s')]
