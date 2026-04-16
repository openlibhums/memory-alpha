from playwright.sync_api import Page, expect
from pelican import get_instance, parse_arguments


pelican, settings = get_instance(parse_arguments())
ALL_PAGES = [
    path for _label, path, target in settings.get('ALL_PAGES') if not target
]

def test_landing_page_internal_links_end_with_html(page: Page, live_server, html_ending_regex):
    page.goto(live_server + "/")
    for locator in page.locator('a:not([target="_blank"]):not([href^="mailto"])').all():
        expect(locator).to_have_attribute("href", html_ending_regex)
