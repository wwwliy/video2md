"""
Provider Factory
"""

import os

from .gemini import GeminiProvider
from .openai import OpenAIProvider


def get_provider():

    provider = (
        os.getenv("AI_PROVIDER", "gemini")
        .lower()
        .strip()
    )

    if provider == "gemini":
        return GeminiProvider()

    if provider == "openai":
        return OpenAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {provider}"
    )