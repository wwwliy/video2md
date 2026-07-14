"""
OpenAI Provider

支持：

- GPT-5.5
- GPT-5
- GPT-4.1
- GPT-4o

兼容官方 OpenAI 与兼容 OpenAI API 的服务商。
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

from ai.providers.base import BaseProvider

load_dotenv()


class OpenAIProvider(BaseProvider):

    def __init__(self):

        self.api_key = os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "OPENAI_API_KEY 未配置，请检查 .env 文件。"
            )

        self.base_url = (
            os.getenv("OPENAI_BASE_URL")
            or "https://api.openai.com/v1"
        )

        self._model = (
            os.getenv("MODEL")
            or "gpt-5.5"
        )

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
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

        messages = []

        if system_prompt.strip():

            messages.append(
                {
                    "role": "system",
                    "content": system_prompt.strip(),
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt.strip(),
            }
        )

        response = self.client.chat.completions.create(
            model=self._model,
            messages=messages,
            temperature=temperature,
        )

        text = response.choices[0].message.content

        if text is None:

            raise RuntimeError(
                "OpenAI 返回为空。"
            )

        return text.strip()