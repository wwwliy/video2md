"""
测试 AIClient
"""

from ai.client import AIClient

client = AIClient()

print("Provider:", client.provider.__class__.__name__)

print()

print("开始测试 AI...")

print()

result = client.ask(
    "请只回复四个字：连接成功"
)

print("=" * 10, "AI 返回", "=" * 10)

print(result)

print("=" * 28)