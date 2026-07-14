"""
AI Processor

负责：

超长 Markdown
        ↓
自动切分
        ↓
AI 整理
        ↓
Markdown 合并
        ↓
去重
        ↓
最终知识库 Markdown
"""

import re
from collections import OrderedDict
from typing import List

from ai.client import AIClient


class AIProcessor:

    def __init__(
        self,
        client: AIClient,
        max_chars: int = 6000,
    ):

        self.client = client
        self.max_chars = max_chars

    # -------------------------------------------------

    def split_text(
        self,
        text: str,
    ) -> List[str]:

        if len(text) <= self.max_chars:
            return [text]

        blocks = []

        current = ""

        for line in text.splitlines():

            if len(current) + len(line) + 1 > self.max_chars:

                if current.strip():
                    blocks.append(current.strip())

                current = line + "\n"

            else:

                current += line + "\n"

        if current.strip():
            blocks.append(current.strip())

        return blocks

    # -------------------------------------------------

    def _unique_lines(
        self,
        lines,
    ):

        result = []

        seen = set()

        for line in lines:

            value = line.strip()

            if not value:
                continue

            if value in seen:
                continue

            seen.add(value)

            result.append(value)

        return result

    # -------------------------------------------------

    def _extract_section(
        self,
        markdown,
        title,
    ):

        pattern = (
            rf"## {re.escape(title)}\n(.*?)(?=\n## |\Z)"
        )

        matches = re.findall(
            pattern,
            markdown,
            flags=re.S,
        )

        return matches

    # -------------------------------------------------

    def _merge_markdown(
        self,
        outputs,
    ):

        if len(outputs) == 1:
            return outputs[0]

        first = outputs[0]

        #
        # 标题
        #

        title = ""

        m = re.search(
            r"^# (.+)$",
            first,
            flags=re.M,
        )

        if m:
            title = m.group(1)

        #
        # 视频信息（仅第一份）
        #

        video_info = ""

        m = re.search(

            r"## 视频信息\n(.*?)(?=\n---)",

            first,

            flags=re.S,

        )

        if m:

            block = m.group(1)

            keep = []

            for line in block.splitlines():

                if line.startswith("链接："):
                    keep.append(line)

                elif line.startswith("采集日期："):
                    keep.append(line)

            video_info = "\n".join(keep)
        #
        # 核心观点
        #

        viewpoints = []

        for output in outputs:

            for block in self._extract_section(
                output,
                "核心观点",
            ):

                for line in block.splitlines():

                    line = line.strip()

                    if (
                        not line
                        or line == "---"
                    ):
                        continue

                    viewpoints.append(line)

        viewpoints = self._unique_lines(
            viewpoints
        )

        #
        # 关键词
        #

        keywords = []

        for output in outputs:

            for block in self._extract_section(
                output,
                "关键词",
            ):

                for line in block.splitlines():

                    line = line.strip()

                    if (
                        not line
                        or line == "---"
                    ):
                        continue

                    keywords.append(line)

        keywords = self._unique_lines(
            keywords
        )

        #
        # 内容整理
        #

        contents = []

        for output in outputs:

            for block in self._extract_section(
                output,
                "内容整理",
            ):

                contents.append(
                    block.strip()
                )

        #
        # 金句
        #

        quotes = []

        for output in outputs:

            for block in self._extract_section(
                output,
                "金句",
            ):

                for line in block.splitlines():

                    line = line.strip()

                    if (
                        not line
                        or line == "---"
                    ):
                        continue

                    quotes.append(line)

        quotes = self._unique_lines(
            quotes
        )

        #
        # 输出 Markdown
        #

        result = []

        if title:

            result.append(
                f"# {title}"
            )

            result.append("")

        result.append(
            "## 视频信息"
        )

        result.append("")

        if video_info:

            result.append(video_info)

        result.append("")

        result.append("---")

        result.append("")

        result.append(
            "## 核心观点"
        )

        result.append("")

        result.extend(viewpoints)

        result.append("")

        result.append("---")

        result.append("")

        result.append(
            "## 关键词"
        )

        result.append("")

        result.extend(keywords)

        result.append("")

        result.append("---")

        result.append("")
        result.append(
            "## 内容整理"
        )

        result.append("")

        for content in contents:

            result.append(content)

            result.append("")

        result.append("---")

        result.append("")

        result.append(
            "## 金句"
        )

        result.append("")

        result.extend(quotes)

        result.append("")

        return "\n".join(result)

    # -------------------------------------------------

    def process(
        self,
        text: str,
        system_prompt: str,
        temperature: float = 0.2,
    ) -> str:

        parts = self.split_text(text)

        outputs = []

        total = len(parts)

        for index, part in enumerate(parts, start=1):

            print()

            print(f"[AI] Processing {index}/{total}")

            result = self.client.ask(

                prompt=part,

                system_prompt=system_prompt,

                temperature=temperature,

            )

            outputs.append(result)

        #
        # 自动合并 Markdown
        #

        return self._merge_markdown(outputs)