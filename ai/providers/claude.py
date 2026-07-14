"""
Claude Provider

支持 Anthropic Claude API。

支持：

- claude-opus-4
- claude-sonnet-4
- 以及后续 Claude 模型

未配置 API Key 时会抛出异常。
"""

import os

from dotenv import load_dotenv
from anthropic import Anthropic

from ai.providers.base import BaseProvider

load_dotenv()


class ClaudeProvider(BaseProvider):

    def __init__(self):

        self.api_key = os.getenv("ANTHROPIC_API_KEY")

        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY 未配置，请检查 .env 文件。"
            )

        self._model = (
            os.getenv("MODEL")
            or "claude-sonnet-4-20250514"
        )

        self.client = Anthropic(
            api_key=self.api_key
        )

    @property
    def model(self):

        return self._model

    def ask(
        self,
        prompt: str,
        system_prompt: str = "",
        temperature: float = 0.3,
    ) -> str:

        response = self.client.messages.create(
            model=self._model,
            max_tokens=8192,
            temperature=temperature,
            system=system_prompt.strip(),
            messages=[
                {
                    "role": "user",
                    "content": prompt.strip(),
                }
            ],
        )

        if not response.content:
            raise RuntimeError(
                "Claude 返回为空。"
            )

        return response.content[0].text.strip()