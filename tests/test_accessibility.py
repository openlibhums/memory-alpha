from playwright.sync_api import Page


def test_main_site_pages_against_wcag(page: Page, live_server, axe, site_page):
    page.goto(live_server + site_page)
    results = axe.run(page)
    if results.violations_count:
        print(results.generate_report())
    assert results.violations_count == 0
