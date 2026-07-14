"""
Markdown Writer

负责：

MarkdownFormatter
        +

AIAnalyzer

↓

最终 Markdown
"""

from datetime import datetime


class MarkdownWriter:

    def build(
        self,
        metadata: dict,
        sections: list,
        ai_result: dict,
    ):

        lines = []

        # ==========================
        # 标题
        # ==========================

        title = metadata.get("title", "未命名视频")

        lines.append(f"# {title}")
        lines.append("")

        # ==========================
        # 视频信息
        # ==========================

        lines.append("## 视频信息")
        lines.append("")

        lines.append(f"平台：{metadata.get('platform','')}")
        lines.append(f"作者：{metadata.get('author','')}")
        lines.append(f"链接：{metadata.get('url','')}")
        lines.append(f"发布日期：{metadata.get('publish_date','')}")
        lines.append(
            f"采集日期：{datetime.now().strftime('%Y-%m-%d')}"
        )
        lines.append(f"时长：{metadata.get('duration','')}")
        lines.append("")
        lines.append("---")
        lines.append("")

        # ==========================
        # AI 核心观点
        # ==========================

        lines.append("## 核心观点")
        lines.append("")

        summary = ai_result.get("summary", [])

        if isinstance(summary, dict):
            summary = summary.get("summary", [])

        for item in summary:
            lines.append(f"- {item}")

        lines.append("")
        lines.append("---")
        lines.append("")

        # ==========================
        # 内容整理
        # ==========================

        lines.append("## 内容整理")
        lines.append("")

        chinese = "一二三四五六七八九十"

        for i, sec in enumerate(sections):

            title = (
                sec.get("title")
                or f"第{chinese[i]}部分"
            )

            lines.append(f"### {title}")
            lines.append("")

            for p in sec["content"]:
                lines.append(p)

            lines.append("")

        lines.append("---")
        lines.append("")

        # ==========================
        # 金句
        # ==========================

        lines.append("## 金句")
        lines.append("")

        quotes = ai_result.get("quotes", [])

        if isinstance(quotes, dict):
            quotes = quotes.get("quotes", [])

        for q in quotes:

            lines.append(f"> {q}")
            lines.append("")

        lines.append("---")
        lines.append("")

        # ==========================
        # 关键词
        # ==========================

        lines.append("## 关键词")
        lines.append("")

        keywords = ai_result.get("keywords", [])

        if isinstance(keywords, dict):
            keywords = keywords.get("keywords", [])

        if keywords:
            lines.append(
                "、".join(keywords)
            )

        lines.append("")

        return "\n".join(lines)