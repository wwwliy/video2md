"""
Knowledge Generator

作用：

Level2 Markdown
        ↓
AI Processor
        ↓
知识库 Markdown

对外只暴露：

    generate(markdown)

    generate_file(path)

"""

from pathlib import Path

from ai.client import AIClient
from ai.processor import AIProcessor
from ai.prompts import SYSTEM_PROMPT


class KnowledgeGenerator:

    def __init__(self):

        self.client = AIClient()

        self.processor = AIProcessor(
            client=self.client,
            max_chars=3000,   # Gemini 免费版安全长度
        )

    # -------------------------------------------------

    def generate(
        self,
        markdown_text: str,
    ) -> str:
        """
        AI 整理知识库
        """

        return self.processor.process(
            text=markdown_text,
            system_prompt=SYSTEM_PROMPT,
            temperature=0.2,
        )

    # -------------------------------------------------

    def generate_file(
        self,
        markdown_file: str,
    ) -> Path:
        """
        输入：
            output/1783868423.md

        输出：
            output/1783868423_ai.md
        """

        markdown_path = Path(markdown_file)

        markdown = markdown_path.read_text(
            encoding="utf-8"
        )

        result = self.generate(markdown)

        output_path = markdown_path.with_name(
            markdown_path.stem + "_ai.md"
        )

        output_path.write_text(
            result,
            encoding="utf-8",
        )

        print()

        print("AI 知识库生成完成：")

        print(output_path)

        return output_path