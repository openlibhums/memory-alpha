import logging


from urllib.parse import urlsplit, urljoin
from playwright.sync_api import Page, expect


logger = logging.getLogger(__name__)


def test_landing_page_internal_links_end_with_html(page: Page, live_server, html_ending_regex):
    page.goto(live_server + "/")
    for locator in page.locator('a:not([target="_blank"]):not([href^="mailto"])').all():
        expect(locator).to_have_attribute("href", html_ending_regex)


def test_internal_links_on_all_pages(page: Page, live_server, axe, subtests):

    visited = {}
    for i, site_page in enumerate(live_server.all_pages):
        page.goto(live_server + site_page)

        # We do not want to test the nav and footer links
        # on every page, just landing pages for each site type
        # (i.e. main and support). So for most pages,
        # we limit the test area to the `main` element
        alpha_site = page.locator('body').get_attribute("data-alpha-site")
        title = page.locator("title")
        prefix = ""
        if alpha_site == "support" and title.inner_text != "Support":
            prefix = "main "
        elif alpha_site == "main" and title.inner_text != "Janeway":
            prefix = "main "

        test_locator = f'{prefix}a:not([target="_blank"]):not([href^="mailto"])'
        for locator in page.locator(test_locator).all():
            href = locator.get_attribute("href")
            if href:
                link = urljoin(live_server + site_page, href)
                if urlsplit(link).netloc not in ["localhost:8000", "127.0.0.1:8000"]:
                    continue

                msg = f"{site_page} -> {locator.inner_text()} {href}"
                with subtests.test(msg=msg, i=i):
                    if link in visited:
                        assert visited[link]
                    else:
                        response = page.request.get(link)
                        visited[link] = response.ok
                        assert response.ok
