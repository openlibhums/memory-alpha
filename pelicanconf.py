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

# The following two lines tell Pelican to reproduce the exact structure
# of the content folder in the output folder (except for pages--specified below)
# We want this so that people can contribute content (including images)
# via the GitHub user interface, using the Preview tab in the markdown editor
# to check the content is rendering as expected.
PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = '{path_no_ext}.html'

# Where to put and serve pages
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Static
STATIC_PATHS = ['docs/images']

# Nav
DISPLAY_PAGES_ON_MENU = False # We want to set the order manually
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('Home', '/'),
    ('Nav1', '/example-page.html'),
    ('Nav2', '/docs/example-docs-page.html'),
]

# jinja2content plugin
JINJA2CONTENT_TEMPLATES = ['content']
