"""
Platform Registry
"""

from platforms.base import PlatformParser
from platforms.douyin import DouyinParser


class PlatformRegistry:
    """Maintain registered platform URL parsers."""

    def __init__(self) -> None:
        """Register built-in platform parsers."""
        self.parsers: list[PlatformParser] = []
        self.register(DouyinParser())

    def register(self, parser: PlatformParser) -> None:
        """Register a platform parser."""
        self.parsers.append(parser)

    def find(self, host: str) -> PlatformParser | None:
        """Return the parser registered for an exact host, if any."""
        for parser in self.parsers:
            if host in parser.domains:
                return parser
        return None
