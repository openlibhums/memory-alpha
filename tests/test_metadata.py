import re
from playwright.sync_api import Page, expect


def test_index_has_title(page: Page, live_server):
    page.goto(live_server + "/")
    expect(page).to_have_title(re.compile("Janeway"))
