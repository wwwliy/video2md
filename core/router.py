"""
Router
"""

from urllib.parse import urlparse

from core.models import UrlInfo
from platforms.registry import PlatformRegistry


class Router:
    """Route URLs to the registered parser for their host."""

    def __init__(self) -> None:
        """Initialize the platform registry."""
        self.registry = PlatformRegistry()

    def parse(self, url: str) -> UrlInfo:
        """Return URL information without raising for unsupported input."""
        host = urlparse(url).netloc.lower()
        parser = self.registry.find(host)
        if parser is not None:
            return parser.parse(url)
        return UrlInfo(
            platform="unknown",
            url_type="unknown",
            original_url=url,
        )
