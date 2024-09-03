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
THEME = 'themes/test'
STYLESHEET_URL = 'theme/css/index.css'

# The following two lines tell Pelican to reproduce the exact structure
# of the content folder in the output folder (except for pages--specified below)
# We want this so that people can contribute content (including images)
# via the GitHub user interface, using the Preview tab in the markdown editor
# to check the content is rendering as expected.
PATH_METADATA = r'(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = '{path_no_ext}.html'

# Where to put and serve pages
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Static
STATIC_PATHS = [
    'docs/images',

    # Legacy paths from old docs
    # that we will eventually remove
    'old-docs/images',
    'old-docs/nstatic',
    'old-docs/nstatic/images',
    'old-docs/nstatic/imports',
    'old-docs/nstatic/image-guidelines',
    'old-docs/nstatic/typesetting',
    'old-docs/nstatic/typesetting/editor',
]

# The following two settings allow us to co-locate component HTML and CSS files in the same folder.
# Prevent HTML files in /components/ from being copied to served assets
IGNORE_FILES = ['/components/*.html']

# Allow us to import component HTML files directly as if they were in /templates/
THEME_TEMPLATES_OVERRIDES = [
    'themes/test/static/',
]

# Nav
DISPLAY_PAGES_ON_MENU = False # We want to set the order manually
DISPLAY_CATEGORIES_ON_MENU = False
LEFT_NAV_ITEMS = [
    ('Our Story', '/'),
    ('Explore', '/example-page.html'),
    ('Hosting', '/docs/example-docs-page.html'),
    ('People', '/docs/example-docs-page.html'),
]
RIGHT_MENU_ITEMS = [
    ('Help/Docs', '/docs-under-construction.html'),
    ('Book a Demo', '/', '')
]

# jinja2content plugin
JINJA2CONTENT_TEMPLATES = ['content']

# Use mtime of files as date in webpage metadata
DEFAULT_DATE = 'fs'

# Take the 'categories' feature and temporarily
# mis-use it to create a working contents tree for docs
CATEGORIES_SAVE_AS = 'docs-under-construction.html'

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.do'],
}

GH_COPYEDIT_CONTENT_URL = 'https://github.com/BirkbeckCTP/memory-alpha/edit/copyediting/content'
