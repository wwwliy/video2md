"""
AI Processor

负责：

超长 Markdown
        ↓
按长度自动切分
        ↓
AI 分段整理
        ↓
再次合并
        ↓
最终知识库 Markdown

为什么需要这一层？

Gemini 免费版、DeepSeek 免费额度、
以及未来部分模型都有 Context 长度限制。

Processor 对上层透明。
KnowledgeGenerator 无需关心模型限制。
"""

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
        """
        按字符长度切分。

        尽量在段落处分割，
        保证上下文连续。
        """

        if len(text) <= self.max_chars:
            return [text]

        blocks = []

        current = ""

        for line in text.splitlines():

            # +1 是换行符
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

    def process(
        self,
        text: str,
        system_prompt: str,
        temperature: float = 0.2,
    ) -> str:
        """
        自动分段调用 AI。

        小文本：
            一次完成

        大文本：
            自动拆分
            自动合并
        """

        parts = self.split_text(text)

        outputs = []

        total = len(parts)

        for index, part in enumerate(parts, start=1):

            print(f"[AI] Processing {index}/{total}")

            result = self.client.ask(
                prompt=part,
                system_prompt=system_prompt,
                temperature=temperature,
            )

            outputs.append(result)

        return "\n\n".join(outputs)