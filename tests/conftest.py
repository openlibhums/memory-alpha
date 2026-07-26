import os
import re
import pytest
from pytest_server import PytestPelicanServer
from axe_playwright_python.sync_playwright import Axe


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


@pytest.fixture(scope="module")
def html_ending_regex():
    return re.compile(r".html")
