import logging
from urllib.parse import urlsplit, urljoin

from playwright.sync_api import Page


logger = logging.getLogger(__name__)


def normalize_path(live_server, site_page, path):
    resource = urljoin(live_server + site_page, path)
    if urlsplit(resource).netloc in ["localhost:8000", "127.0.0.1:8000"]:
        return resource
    else:
        return ""


def test_all_pages(page: Page, live_server, axe, subtests):
    visited = {}
    for i, site_page in enumerate(live_server.all_pages):

        # Test WCAG
        page.goto(live_server + site_page)
        msg = f"WCAG failure: {site_page}"
        with subtests.test(msg=msg, i=i):
            results = axe.run(page)
            if results.violations_count:
                logger.warning(results.generate_report())
            assert results.violations_count == 0

        # Test broken links
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
            text = locator.inner_text()
            msg = f"Broken link: {site_page} -> {text} {href}"
            with subtests.test(msg=msg, i=i):
                assert href
                link = normalize_path(live_server, site_page, href)
                if not link:
                    continue

                if link in visited:
                    assert visited[link]
                else:
                    response = page.request.get(link)
                    visited[link] = response.ok
                    assert response.ok

        # Test broken images
        test_locator = f'{prefix}img'
        for locator in page.locator(test_locator).all():
            src = locator.get_attribute("src")
            alt = locator.get_attribute("alt")
            msg = f"Broken image: {site_page} -> {alt} {src}"
            with subtests.test(msg=msg, i=i):
                img = normalize_path(live_server, site_page, src)
                if not img:
                    continue

                if img in visited:
                    assert visited[img]
                else:
                    response = page.request.get(img)
                    visited[img] = response.ok
                    assert response.ok
