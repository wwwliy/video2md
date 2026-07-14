from pathlib import Path

from ai.analyzer import AIAnalyzer


# 找 output 下最新 txt
output_dir = Path("output")

txt_files = sorted(
    output_dir.glob("*.txt"),
    key=lambda x: x.stat().st_mtime,
    reverse=True,
)

if not txt_files:
    raise FileNotFoundError("output 目录没有 txt 文件")

txt_file = txt_files[0]

print("读取：", txt_file)

text = txt_file.read_text(
    encoding="utf-8"
)

analyzer = AIAnalyzer()

result = analyzer.analyze(text)

print("\n====================")
print(result)
print("====================")