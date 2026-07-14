"""
Render MergeResult into final Markdown.
"""

from __future__ import annotations

from ai.schemas import MergeResult


class MarkdownRenderer:
    """
    Render MergeResult to markdown.
    """

    def render(
        self,
        result: MergeResult,
    ) -> str:

        lines: list[str] = []

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        if result.title:

            lines.append(f"# {result.title}")

        else:

            lines.append("# AI知识整理")

        lines.append("")

        # -------------------------------------------------
        # Video Info
        # -------------------------------------------------

        lines.append("## 视频信息")
        lines.append("")

        if result.video_info.url:

            lines.append(
                f"- 视频链接：{result.video_info.url}"
            )

        if result.video_info.collected_at:

            lines.append(
                f"- 采集时间：{result.video_info.collected_at}"
            )

        lines.append("")

        # -------------------------------------------------
        # Core Viewpoints
        # -------------------------------------------------

        if result.viewpoints:

            lines.append("## 核心观点")
            lines.append("")

            for item in result.viewpoints:

                lines.append(f"- {item}")

            lines.append("")

        # -------------------------------------------------
        # Keywords
        # -------------------------------------------------

        if result.keywords:

            lines.append("## 关键词")
            lines.append("")

            keyword_line = "、".join(result.keywords)

            lines.append(keyword_line)

            lines.append("")

        # -------------------------------------------------
        # Content
        # -------------------------------------------------

        if result.contents:

            lines.append("## 内容整理")
            lines.append("")

            for paragraph in result.contents:

                lines.append(paragraph)

                lines.append("")

        # -------------------------------------------------
        # Quotes
        # -------------------------------------------------

        if result.quotes:

            lines.append("## 金句")
            lines.append("")

            for quote in result.quotes:

                lines.append(f"> {quote}")

                lines.append("")

        return "\n".join(lines).rstrip() + "\n"