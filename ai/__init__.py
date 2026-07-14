"""
Video2MD AI Module

统一导出 AI 模块。

目前支持：

- Gemini
- OpenAI
- Claude
- DeepSeek

主要组件：

AIClient
AIProcessor
KnowledgeGenerator
"""

"""
Video2MD AI Module
"""

from ai.client import AIClient
from ai.processor import AIProcessor
from ai.knowledge_generator import KnowledgeGenerator

__version__ = "1.0.0"

__all__ = [
    "AIClient",
    "AIProcessor",
    "KnowledgeGenerator",
]