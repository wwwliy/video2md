from pathlib import Path

from formatter.markdown_formatter import MarkdownFormatter

txt_file = Path("output/1783868423.txt")

text = txt_file.read_text(
    encoding="utf-8"
)

formatter = MarkdownFormatter()

formatter.generate(
    text=text,
    video_info={
        "title": "TikTok投流分享",
        "platform": "Douyin",
        "author": "",
        "url": "",
        "publish_date": "",
        "duration": ""
    },
    output_file="output/1783868423.md"
)

print("Markdown 生成完成。")