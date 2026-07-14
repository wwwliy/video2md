"""
AI Client

统一 AI 调用入口。

支持：

- Gemini
- OpenAI
- Claude
- DeepSeek

通过 .env 配置：

AI_PROVIDER=gemini
"""

import os

from dotenv import load_dotenv

load_dotenv()


class AIClient:

    def __init__(self):

        provider = (
            os.getenv("AI_PROVIDER", "gemini")
            .strip()
            .lower()
        )

        self.provider_name = provider

        # -----------------------------
        # Lazy Import
        # -----------------------------

        if provider == "gemini":

            from ai.providers.gemini import GeminiProvider

            self.provider = GeminiProvider()

        elif provider == "openai":

            from ai.providers.openai import OpenAIProvider

            self.provider = OpenAIProvider()

        elif provider == "claude":

            from ai.providers.claude import ClaudeProvider

            self.provider = ClaudeProvider()

        elif provider == "deepseek":

            from ai.providers.deepseek import DeepSeekProvider

            self.provider = DeepSeekProvider()

        else:

            raise ValueError(
                f"未知 AI_PROVIDER：{provider}"
            )

    # -----------------------------------------------------

    def ask(
        self,
        prompt,
        system_prompt="",
        temperature=0.3,
    ):

        return self.provider.ask(
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=temperature,
        )

    # -----------------------------------------------------

    @property
    def model(self):

        return getattr(
            self.provider,
            "model",
            "Unknown",
        )

    # -----------------------------------------------------

    def __repr__(self):

        return (
            f"<AIClient "
            f"provider={self.provider_name} "
            f"model={self.model}>"
        )