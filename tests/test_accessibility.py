import logging
from urllib.parse import urlsplit, urljoin

from playwright.sync_api import Page


logger = logging.getLogger(__name__)


def normalize_path(page_being_tested, path):
    resource = urljoin(page_being_tested, path)
    if urlsplit(resource).netloc in ["localhost:8000", "127.0.0.1:8000"]:
        return resource
    else:
        return ""


def test_all_pages(page: Page, live_server, axe, subtests):
    visited = {}
    for i, site_page in enumerate(live_server.all_pages):
        page_being_tested = live_server + site_page

        # Test WCAG
        page.goto(page_being_tested)
        msg = f"WCAG failure: {site_page}"
        with subtests.test(msg=msg, i=i):
            results = axe.run(page)
            if results.violations_count:
                logger.warning(results.generate_report())
            assert results.violations_count == 0

        # Prepare to test image paths and links.
        # We do not want to test the nav and footer links
        # on every page, just landing pages for each site type
        # (i.e. main and support). So for most pages,
        # we limit the test area to the `main` element.
        alpha_site = page.locator('body').get_attribute("data-alpha-site")
        title = page.locator("title")
        prefix = ""
        if alpha_site == "support" and title.inner_text != "Support":
            prefix = "main "
        elif alpha_site == "main" and title.inner_text != "Janeway":
            prefix = "main "

        # Test broken images
        test_locator = f'{prefix}img'
        for locator in page.locator(test_locator).all():
            src = locator.get_attribute("src")
            alt = locator.get_attribute("alt")
            img = normalize_path(page_being_tested, src)
            if not img:
                continue

            if img in visited:
                ok, msg = visited[img]
                with subtests.test(msg=msg, i=i):
                    assert ok
            else:
                msg = f"Broken image: {site_page} -> {alt} {src}"
                with subtests.test(msg=msg, i=i):
                    response = page.request.get(img)
                    visited[img] = response.ok, msg
                    assert response.ok

        # Test links
        test_locator = f'{prefix}a:not([target="_blank"]):not([href^="mailto"])'
        for locator in page.locator(test_locator).all():
            href = locator.get_attribute("href")
            text = locator.inner_text()
            fragment = urlsplit(href).fragment
            link = normalize_path(page_being_tested, href)
            if not link:
                continue

            if link in visited:
                ok, msg = visited[link]
                with subtests.test(msg=msg, i=i):
                    assert ok

            elif fragment:
                separate_page = bool(urlsplit(href).path)
                if separate_page:
                    page.goto(link)

                target = page.locator(f'#{fragment}')
                target_count = target.count()
                if target_count > 1:
                    msg = f"Link to duplicate headings: {site_page} -> {text} {href}"
                elif target_count < 1:
                    msg = f"Broken heading link: {site_page} -> {text} {href}"
                with subtests.test(msg=msg, i=i):
                    one_target = target_count == 1
                    assert one_target
                    visited[link] = one_target, msg

                if separate_page:
                    page.goto(page_being_tested)

            else:
                msg = f"Broken page link: {site_page} -> {text} {href}"
                with subtests.test(msg=msg, i=i):
                    response = page.request.get(link)
                    assert response.ok
                    visited[link] = response.ok, msg
