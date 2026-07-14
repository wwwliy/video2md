from pathlib import Path
from datetime import datetime

from formatter.section_splitter import SectionSplitter


class MarkdownFormatter:

    def __init__(self):
        self.splitter = SectionSplitter()

    def generate(
        self,
        text: str,
        video_info: dict = None,
        output_file: str = None,
    ) -> str:

        if video_info is None:
            video_info = {}

        title = video_info.get("title", "未命名视频")
        platform = video_info.get("platform", "")
        author = video_info.get("author", "")
        url = video_info.get("url", "")
        publish_date = video_info.get("publish_date", "")
        duration = video_info.get("duration", "")

        collect_date = datetime.now().strftime("%Y-%m-%d")

        # 自动分段
        sections = self.splitter.split(text)

        md = []

        # ==========================
        # 标题
        # ==========================

        md.append(f"# {title}")
        md.append("")

        # ==========================
        # 视频信息
        # ==========================

        md.append("## 视频信息")
        md.append("")

        md.append(f"平台：{platform}")
        md.append("")
        md.append(f"作者：{author}")
        md.append("")
        md.append(f"链接：{url}")
        md.append("")
        md.append(f"发布日期：{publish_date}")
        md.append("")
        md.append(f"采集日期：{collect_date}")
        md.append("")
        md.append(f"时长：{duration}")
        md.append("")

        md.append("---")
        md.append("")

        # ==========================
        # 核心观点（后续AI）
        # ==========================

        md.append("## 核心观点")
        md.append("")
        md.append("> （待 AI 总结）")
        md.append("")

        md.append("---")
        md.append("")

        # ==========================
        # 内容整理
        # ==========================

        md.append("## 内容整理")
        md.append("")

        chinese_numbers = [
            "一",
            "二",
            "三",
            "四",
            "五",
            "六",
            "七",
            "八",
            "九",
            "十",
            "十一",
            "十二",
            "十三",
            "十四",
            "十五",
        ]

        for i, section in enumerate(sections):

            if i < len(chinese_numbers):
                idx = chinese_numbers[i]
            else:
                idx = str(i + 1)

            title = section["title"]

            if title.startswith("主题"):
                md.append(f"### {idx}、")
            else:
                md.append(f"### {idx}、{title}")

            md.append("")
            md.append(section["content"])
            md.append("")

        md.append("---")
        md.append("")

        # ==========================
        # 金句（后续AI）
        # ==========================

        md.append("## 金句")
        md.append("")
        md.append("> （待 AI 提取）")
        md.append("")
        md.append("> （待 AI 提取）")
        md.append("")

        markdown = "\n".join(md)

        if output_file:

            output_path = Path(output_file)

            output_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            output_path.write_text(
                markdown,
                encoding="utf-8",
            )

        return markdown