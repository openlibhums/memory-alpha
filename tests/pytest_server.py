import os
import threading
from urllib.parse import urlparse

from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican import (
    get_instance as get_pelican_instance,
    parse_arguments as parse_pelican_arguments
)


class LiveServerThread(threading.Thread):
    """Thread for running a live HTTP server while the tests are running.

    Based on Django LiveServerThread.
    """

    def __init__(self, host, port, output):
        self.host = host
        self.port = port
        self.output = output
        self.httpd = RootedHTTPServer(
            self.output,
            (self.host, self.port),
            ComplexHTTPRequestHandler,
        )
        self.is_ready = threading.Event()
        self.error = None
        super().__init__()

    def run(self):
        try:
            self.is_ready.set()
            self.httpd.serve_forever()
        except Exception as e:
            self.error = e
            self.is_ready.set()

    def terminate(self):
        if hasattr(self, "httpd"):
            self.httpd.shutdown()
            self.httpd.server_close()
        self.join()


class PytestPelicanServer:
    """The liveserver fixture

    Adapted from the live server helper in pytest-django.

    This is the object that the ``live_server`` fixture returns.
    The ``live_server`` fixture handles creation and stopping.
    """

    def __init__(
        self,
        addr: str,
        *,
        start: bool = True,
        output: str = 'output',
    ) -> None:
        self.parsed_url = urlparse(addr)
        self.thread = LiveServerThread(
            self.parsed_url.hostname,
            port=int(self.parsed_url.port or 0),
            output=output,
        )
        self.thread.daemon = True
        self.pelican, self.pelican_settings = get_pelican_instance(
            parse_pelican_arguments(["-l",])
        )
        self.pelican_settings["TESTING"] = True

        if start:
            self.start()

    def start(self) -> None:
        """Start the server"""
        self.thread.start()
        self.thread.is_ready.wait()
        self.pelican.run()

        if self.thread.error:
            error = self.thread.error
            self.stop()
            raise error

    def stop(self) -> None:
        """Stop the server"""
        self.thread.terminate()

    def get_main_pages(self):
        main_pages = []
        for _label, path, target in self.pelican_settings.get('ALL_PAGES'):
            if not target:
                main_pages.append(path)
        return main_pages

    def get_support_pages(self):
        support_pages = []
        support_content_path = self.pelican_settings.get("SUPPORT_CONTENT_PATH")
        for dirpath, dirnames, filenames in os.walk(support_content_path):
            for filename in filenames:
                if filename.endswith(".md"):
                    filename = filename[:-3] + ".html"
                    content_path = os.path.join(dirpath, filename)
                    pelican_path = self.pelican_settings.get("PATH")
                    rel_path = os.path.relpath(content_path, start=pelican_path)
                    support_pages.append("/" + rel_path)
        return support_pages

    @property
    def all_pages(self):
        return self.get_main_pages() + self.get_support_pages()

    @property
    def url(self) -> str:
        return f"http://{self.thread.host}:{self.thread.port}"

    def __str__(self) -> str:
        return self.url

    def __add__(self, other) -> str:
        return f"{self}{other}"

    def __repr__(self) -> str:
        return f"<PytestPelicanServer listening at {self.url}>"
