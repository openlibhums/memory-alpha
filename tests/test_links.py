import logging


from playwright.sync_api import Page, expect


logger = logging.getLogger(__name__)


def test_landing_page_internal_links_end_with_html(page: Page, live_server, html_ending_regex):
    page.goto(live_server + "/")
    for locator in page.locator('a:not([target="_blank"]):not([href^="mailto"])').all():
        expect(locator).to_have_attribute("href", html_ending_regex)
