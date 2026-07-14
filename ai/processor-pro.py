"""
AI Processor

负责：

1. 长文本切分
2. AI 分段调用
3. 保存每段缓存
4. 已完成部分自动跳过
5. 合并最终结果
"""

from pathlib import Path

from ai.client import AIClient


class AIProcessor:

    def __init__(
        self,
        client=None,
        max_chars=3000,
    ):

        self.client = client or AIClient()

        self.max_chars = max_chars

    # --------------------------------------------------

    def split_text(
        self,
        text,
    ):

        """
        按字符数切分。

        尽量在空行处分段。
        """

        if len(text) <= self.max_chars:
            return [text]

        parts = []

        start = 0

        while start < len(text):

            end = start + self.max_chars

            if end >= len(text):

                parts.append(
                    text[start:]
                )

                break

            split = text.rfind(
                "\n\n",
                start,
                end,
            )

            if split == -1:

                split = end

            parts.append(
                text[start:split]
            )

            start = split

        return parts

    # --------------------------------------------------

    def process(
        self,
        text,
        system_prompt="",
        temperature=0.2,
        cache_dir="output/.cache",
        task_name="knowledge",
    ):
        cache_path = Path(cache_dir)

        cache_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        parts = self.split_text(text)

        outputs = []

        total = len(parts)

        for index, part in enumerate(parts):

            print(
                f"\n[AI] Processing {index + 1}/{total}"
            )

            part_file = cache_path / (
                f"{task_name}_part_{index + 1}.md"
            )

            #
            # 已存在缓存
            #
            if part_file.exists():

                print(
                    f"✓ 使用缓存：{part_file.name}"
                )

                outputs.append(
                    part_file.read_text(
                        encoding="utf-8"
                    )
                )

                continue

            #
            # 调用 AI
            #
            result = self.client.ask(
                prompt=part,
                system_prompt=system_prompt,
                temperature=temperature,
            )
            #
            # 保存当前 Part
            #
            part_file.write_text(
                result,
                encoding="utf-8",
            )

            print(
                f"✓ 已保存：{part_file.name}"
            )

            outputs.append(result)

        #
        # 合并所有 Part
        #
        print("\n开始合并所有 AI 输出...")

        merged = "\n\n".join(outputs)

        return merged
