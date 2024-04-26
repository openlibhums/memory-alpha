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
STYLESHEET_URL = '/output.css'

# Tailwind
TAILWIND = {
    "version": "3.4.3",
    "plugins": [],
}

# The following two lines tell Pelican to reproduce the exact structure
# of the content folder in the output folder.
# We want this so that people can contribute content (including images)
# via the GitHub user interface, using the Preview tab in the markdown editor
# to check the content is rendering as expected.
PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'

# Static
STATIC_PATHS = ['docs/images']

# Nav
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('Nav1', '/'),
    ('Nav2', '/docs/example.html'),
]
