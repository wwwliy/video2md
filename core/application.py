"""Application workflow controller and command-line interface."""

import argparse
from collections.abc import Sequence

from core.router import Router


class Application:
    """Coordinate application services and command-line input."""

    def __init__(self) -> None:
        """Initialize application services."""
        self.router = Router()

    def run(self, arguments: Sequence[str] | None = None) -> None:
        """Parse the URL argument and print its parsed information."""
        parser = argparse.ArgumentParser(description="Parse a video platform URL.")
        parser.add_argument("url", help="Video or account URL to parse.")
        args = parser.parse_args(arguments)
        info = self.router.parse(args.url)

        print(f"Platform : {info.platform}")
        print(f"Type : {info.url_type}")
        print(f"ID : {info.resource_id}")
        print("------------------------------------")
