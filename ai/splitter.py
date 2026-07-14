"""
Text splitter for AI processing.

负责：

Markdown
    ↓
智能切分
    ↓
多个文本块

尽量保持标题完整，不在 Markdown 标题中间切分。
"""

from __future__ import annotations

from typing import List


class TextSplitter:
    """
    Split markdown text into several chunks.

    Parameters
    ----------
    max_chars
        Maximum characters for each chunk.
    """

    def __init__(self, max_chars: int = 3500):

        self.max_chars = max_chars

    def split(self, text: str) -> List[str]:
        """
        Split markdown into chunks.

        Parameters
        ----------
        text
            Markdown content.

        Returns
        -------
        list[str]
        """

        text = text.strip()

        if len(text) <= self.max_chars:
            return [text]

        paragraphs = text.split("\n\n")

        parts: List[str] = []

        current: List[str] = []

        current_length = 0

        for para in paragraphs:

            para = para.strip()

            if not para:
                continue

            para_length = len(para) + 2

            if current and current_length + para_length > self.max_chars:

                parts.append("\n\n".join(current))

                current = []

                current_length = 0

            current.append(para)

            current_length += para_length

        if current:

            parts.append("\n\n".join(current))

        return parts

    def count(self, text: str) -> int:
        """
        Return number of chunks.

        Parameters
        ----------
        text
            Markdown text.

        Returns
        -------
        int
        """

        return len(self.split(text))

    def preview(self, text: str) -> None:
        """
        Print split information.

        Useful during debugging.
        """

        parts = self.split(text)

        print()

        print("=" * 60)
        print("Text Splitter")
        print("=" * 60)

        print(f"Total Parts : {len(parts)}")

        for i, part in enumerate(parts, start=1):

            print(
                f"Part {i:<2} "
                f"{len(part):>5} chars"
            )

        print("=" * 60)