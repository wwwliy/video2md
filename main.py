"""
Video2MD

统一入口

python main.py "视频链接"
"""

import sys
from pathlib import Path

from downloader.downloader import Downloader
from transcriber.whisper_transcriber import WhisperTranscriber
from formatter.markdown_formatter import MarkdownFormatter
from ai.knowledge_generator import KnowledgeGenerator


def main():

    if len(sys.argv) != 2:

        print()
        print("Usage:")
        print('python main.py "video_url"')
        print()

        return

    url = sys.argv[1]

    print("\n" + "=" * 60)
    print("Video2MD")
    print("=" * 60)

    #
    # Step 1
    #

    print("\n[1/4] Download Video")

    downloader = Downloader()

    video_path = downloader.download(url)

    if video_path is None:

        print("Download failed.")

        return

    print(f"✓ {video_path}")

    #
    # Step 2
    #

    print("\n[2/4] Whisper")

    whisper = WhisperTranscriber()

    whisper.transcribe(str(video_path))

    txt_file = Path("output") / (video_path.stem + ".txt")

    print(f"✓ {txt_file}")

    #
    # Step 3
    #

    print("\n[3/4] Markdown")

    formatter = MarkdownFormatter()

    formatter.generate(

        text=txt_file.read_text(
            encoding="utf-8"
        ),

        video_info={

            "title": "",

            "platform": "",

            "author": "",

            "url": url,

            "publish_date": "",

            "duration": ""

        },

        output_file=str(
            Path("output") /
            (video_path.stem + ".md")
        )

    )

    md_file = Path("output") / (video_path.stem + ".md")

    print(f"✓ {md_file}")

    #
    # Step 4
    #

    print("\n[4/4] AI Knowledge")

    generator = KnowledgeGenerator()

    ai_file = generator.generate_file(
        md_file
    )

    print(f"✓ {ai_file}")

    print("\n" + "=" * 60)
    print("Finished")
    print("=" * 60)

    print()

    print(video_path)

    print(txt_file)

    print(md_file)

    print(ai_file)

    print()


if __name__ == "__main__":

    main()