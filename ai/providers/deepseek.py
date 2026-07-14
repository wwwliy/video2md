"""
DeepSeek Provider

支持：

- DeepSeek Chat
- DeepSeek Reasoner

兼容 DeepSeek 官方 API
以及 OpenAI Compatible API。
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

from ai.providers.base import BaseProvider

load_dotenv()


class DeepSeekProvider(BaseProvider):

    def __init__(self):

        self.api_key = os.getenv("DEEPSEEK_API_KEY")

        if not self.api_key:
            raise ValueError(
                "DEEPSEEK_API_KEY 未配置，请检查 .env 文件。"
            )

        self.base_url = (
            os.getenv("DEEPSEEK_BASE_URL")
            or "https://api.deepseek.com/v1"
        )

        self._model = (
            os.getenv("MODEL")
            or "deepseek-chat"
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
                "DeepSeek 返回为空。"
            )

        return text.strip()