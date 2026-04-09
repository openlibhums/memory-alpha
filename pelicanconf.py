from datetime import datetime
import logging


AUTHOR = 'Open Library of Humanities'
SITENAME = 'Janeway Systems'
SITEURL = ""

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
ARTICLE_URL = ARTICLE_SAVE_AS = '{path_no_ext}.html'

# Where to put and serve pages
# PAGE_URL = '{slug}.html'
# PAGE_SAVE_AS = '{slug}.html'

# Static
STATIC_PATHS = [
    'support/images',
    'support/downloadables',

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
    ('Our Story', '/pages/our-story.html', ""),
    # ('Explore', '#', ''), Not in scope for MVP
    ('Hosting', '#', ""),
    # ('People', '#', ''), Not in scope for MVP
]
RIGHT_NAV_ITEMS = [
    # ('Book a Demo', '#', '') Not in scope for MVP
    ('Support', '/support/under-construction.html', "_blank"),
    ('Source Code', 'https://github.com/openlibhums/janeway', "_blank"),
]
ALL_PAGES =  [
    ('Home', '/', ""),
] + LEFT_NAV_ITEMS + RIGHT_NAV_ITEMS

# jinja2content plugin
JINJA2CONTENT_TEMPLATES = [
    'pages',
    'support',
    'old-docs', # temporary until new docs are complete
]

# Use mtime of files as date in webpage metadata
DEFAULT_DATE = 'fs'

# Take the 'categories' feature and temporarily
# mis-use it to create a working contents tree for docs
CATEGORIES_SAVE_AS = 'support/under-construction.html'

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.do'],
}

JINJA_GLOBALS = {
    "current_year": datetime.now().strftime("%Y"),
}

GH_MAIN_CONTENT_URL = 'https://github.com/BirkbeckCTP/memory-alpha/edit/main/content'
GH_COPYEDIT_CONTENT_URL = 'https://github.com/BirkbeckCTP/memory-alpha/edit/copyediting/content'

# Filter out empty alt warnings, which do not account for the primary method of
# marking images as decorative, which is alt=""
LOG_FILTER = [(logging.WARN, 'Empty alt attribute for image %s in %s')]
