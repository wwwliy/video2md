"""
generate.py

命令行入口

用法：

python -m ai.generate output/1783868423.md

输出：

output/1783868423_ai.md
"""

import sys
from pathlib import Path

from ai.knowledge_generator import KnowledgeGenerator


def main():

    if len(sys.argv) != 2:

        print()

        print("Usage:")

        print("python -m ai.generate output/xxxx.md")

        print()

        return

    input_file = Path(sys.argv[1])

    if not input_file.exists():

        print()

        print("文件不存在：")

        print(input_file)

        print()

        return

    print()

    print("=" * 60)

    print("Video2MD AI Knowledge Generator")

    print("=" * 60)

    print()

    print("输入文件：")

    print(input_file)

    print()

    generator = KnowledgeGenerator()

    output_file = generator.generate_file(
        input_file
    )

    print()

    print("=" * 60)

    print("生成完成")

    print("=" * 60)

    print()

    print("输出文件：")

    print(output_file)

    print()


if __name__ == "__main__":

    main()