"""
URL input.
"""

from urllib.parse import urlparse


class UrlInput:
    """
    Handle URL input.
    """

    def can_handle(self, source: str) -> bool:

        try:

            result = urlparse(source)

            return result.scheme in ("http", "https")

        except Exception:

            return False