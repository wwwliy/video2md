"""
Input manager.
"""

from pathlib import Path

from input.local import LocalInput
from input.url import UrlInput


class InputManager:
    """
    Decide input type.
    """

    def __init__(self):

        self.local = LocalInput()

        self.url = UrlInput()

    def is_local(self, source: str) -> bool:

        return self.local.can_handle(source)

    def is_url(self, source: str) -> bool:

        return self.url.can_handle(source)

    def load_local(self, source: str) -> Path:

        return self.local.load(source)