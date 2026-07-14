"""
AI Processor

Pipeline

Markdown
    ↓
TextSplitter
    ↓
AI Client
    ↓
MarkdownParser
    ↓
KnowledgeMerger
    ↓
MarkdownRenderer
"""

from __future__ import annotations

from ai.client import AIClient

from ai.splitter import TextSplitter
from ai.parser import MarkdownParser
from ai.merger import KnowledgeMerger
from ai.renderer import MarkdownRenderer


class AIProcessor:
    """
    Main AI pipeline.
    """

    def __init__(
        self,
        client: AIClient,
        max_chars: int = 3500,
    ):

        self.client = client

        self.splitter = TextSplitter(
            max_chars=max_chars
        )

        self.parser = MarkdownParser()

        self.merger = KnowledgeMerger()

        self.renderer = MarkdownRenderer()

    # --------------------------------------------------

    def process(
        self,
        text: str,
        system_prompt: str,
        temperature: float = 0.2,
    ) -> str:
        """
        Process markdown.

        Markdown

            ↓

        Split

            ↓

        AI

            ↓

        Parse

            ↓

        Merge

            ↓

        Render
        """

        #
        # Split
        #

        parts = self.splitter.split(text)

        total = len(parts)

        documents = []

        #
        # AI
        #

        for index, part in enumerate(parts, start=1):

            print()

            print(
                f"[AI] Processing {index}/{total}"
            )

            markdown = self.client.ask(

                prompt=part,

                system_prompt=system_prompt,

                temperature=temperature,

            )

            #
            # Parse
            #

            document = self.parser.parse(
                markdown
            )

            documents.append(document)

        #
        # Merge
        #

        merged = self.merger.merge(
            documents
        )

        #
        # Render
        #

        return self.renderer.render(
            merged
        )