"""
测试：

TXT
↓

AI Analyzer

↓

Markdown Writer

↓

Markdown 文件
"""

from pathlib import Path

from ai.analyzer import AIAnalyzer
from formatter.section_splitter import SectionSplitter
from formatter.markdown_writer import MarkdownWriter


# ==========================
# TXT 文件
# ==========================

txt_file = Path(
    "output/1783868423.txt"
)

print("读取：", txt_file)

text = txt_file.read_text(
    encoding="utf-8"
)

print("文本长度：", len(text))


# ==========================
# AI 分析
# ==========================

print("\n开始 AI 分析...\n")

analyzer = AIAnalyzer()

ai_result = analyzer.analyze(text)

print("AI 分析完成。")


# ==========================
# 自动分段
# ==========================

splitter = SectionSplitter()

sections = splitter.split(text)

print("章节数量：", len(sections))


# ==========================
# 视频信息（先手动）
# ==========================

metadata = {

    "title": "TikTok投流分享",

    "platform": "Douyin",

    "author": "",

    "url": "",

    "publish_date": "",

    "duration": "",

}


# ==========================
# Markdown
# ==========================

writer = MarkdownWriter()

markdown = writer.build(
    metadata=metadata,
    sections=sections,
    ai_result=ai_result,
)


# ==========================
# 保存
# ==========================

output_file = Path(
    "output/1783868423.md"
)

output_file.write_text(
    markdown,
    encoding="utf-8"
)

print("\n========================")
print("Markdown 已生成：")
print(output_file)
print("========================")