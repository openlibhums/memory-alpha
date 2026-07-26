from playwright.sync_api import Page


def test_main_site_pages_against_wcag(page: Page, live_server, axe, subtests):
    for i, each in enumerate(live_server.all_pages):
        with subtests.test(msg=each, i=i):
            page.goto(live_server + each)
            results = axe.run(page)
            if results.violations_count:
                print(results.generate_report())
            assert results.violations_count == 0
