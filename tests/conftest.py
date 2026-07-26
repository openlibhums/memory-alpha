import logging
import os
import re
import pytest
from pytest_server import PytestPelicanServer
from pelican import get_instance, parse_arguments
from axe_playwright_python.sync_playwright import Axe


def get_support_pages():
    support_pages = []
    support_content_path = settings.get("SUPPORT_CONTENT_PATH")
    for dirpath, dirnames, filenames in os.walk(support_content_path):
        for filename in filenames:
            if filename.endswith(".md"):
                filename = filename[:-3] + ".html"
                content_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(content_path, start=settings.get("PATH"))
                support_pages.append("/" + rel_path)
    return support_pages


pelican, settings = get_instance(parse_arguments())
ALL_PAGES = [
    path for _label, path, target in settings.get('ALL_PAGES') if not target
] + get_support_pages()


@pytest.fixture(scope="session")
def live_server(base_url: str):
    """Run a live Pelican server in the background during tests

    The address the server is started from is taken from the
    the PELICAN_LIVE_TEST_SERVER_ADDRESS environment variable or
    if this is not provided then the base_url setting in pytest.ini.
    If neither is provided ``localhost`` is used.
    """

    addr = (
        os.getenv("PELICAN_LIVE_TEST_SERVER_ADDRESS")
        or base_url
        or "localhost"
    )

    server = PytestPelicanServer(addr)
    yield server
    server.stop()


@pytest.fixture(scope="module")
def axe():
    return Axe()


@pytest.fixture(scope="module", params=ALL_PAGES)
def site_page(request):
    yield request.param


@pytest.fixture(scope="module")
def html_ending_regex():
    return re.compile(r".html")
