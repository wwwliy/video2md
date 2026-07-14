"""
Merge multiple KnowledgeDocument objects.

Video2MD AI Pipeline

KnowledgeDocument
        ↓
KnowledgeDocument
        ↓
KnowledgeDocument
        ↓
KnowledgeMerger
        ↓
MergeResult
"""

from __future__ import annotations

from ai.schemas import (
    KnowledgeDocument,
    MergeResult,
)


class KnowledgeMerger:
    """
    Merge multiple KnowledgeDocument objects.
    """

    def merge(
        self,
        documents: list[KnowledgeDocument],
    ) -> MergeResult:

        result = MergeResult()

        for doc in documents:

            # -------------------------
            # 标题
            # -------------------------

            if not result.title and doc.title:

                result.title = doc.title

            # -------------------------
            # 视频信息
            # -------------------------

            if (
                not result.video_info.url
                and doc.video_info.url
            ):

                result.video_info.url = (
                    doc.video_info.url
                )

            if (
                not result.video_info.collected_at
                and doc.video_info.collected_at
            ):

                result.video_info.collected_at = (
                    doc.video_info.collected_at
                )

            # -------------------------
            # 内容
            # -------------------------

            result.viewpoints.extend(
                doc.viewpoints
            )

            result.keywords.extend(
                doc.keywords
            )

            result.contents.extend(
                doc.contents
            )

            result.quotes.extend(
                doc.quotes
            )

        # 去重

        result.viewpoints = self._unique(
            result.viewpoints
        )

        result.keywords = self._unique(
            result.keywords
        )

        result.contents = self._unique(
            result.contents
        )

        result.quotes = self._unique(
            result.quotes
        )

        return result

    # ---------------------------------------------------

    @staticmethod
    def _unique(
        items: list[str],
    ) -> list[str]:

        result = []

        seen = set()

        for item in items:

            item = item.strip()

            if not item:

                continue

            if item in seen:

                continue

            seen.add(item)

            result.append(item)

        return result