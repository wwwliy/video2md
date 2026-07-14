"""
测试完整知识库生成
"""

from ai.knowledge_generator import KnowledgeGenerator

generator = KnowledgeGenerator()

generator.generate_file(
    "output/1783868423.md"
)