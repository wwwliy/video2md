"""
测试 AIProcessor 自动分段
"""

from ai.client import AIClient
from ai.processor import AIProcessor

client = AIClient()

processor = AIProcessor(
    client=client,
    max_chars=1000,
)

text = "你好。\n" * 3000

parts = processor.split_text(text)

print()

print("总长度：", len(text))

print("切成：", len(parts), "段")

print()

for i, p in enumerate(parts, 1):

    print(i, len(p))