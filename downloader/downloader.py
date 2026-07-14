"""
Unified Video Downloader

入口：

Downloader().download(url)

负责：

1. 判断平台
2. 选择 Provider
3. 下载视频
"""

from pathlib import Path

from downloader.platform_detector import get_greenvideo_page
from downloader.providers.greenvideo import GreenVideoDownloader


class Downloader:

    def __init__(self, output_dir="output/downloads"):

        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def download(self, url: str) -> Path:

        print("\n==========================")
        print("Platform Detect")
        print("==========================")

        page = get_greenvideo_page(url)

        print(page)

        print("\n==========================")
        print("Downloader")
        print("==========================")

        #
        # 目前统一使用 GreenVideo
        #

        downloader = GreenVideoDownloader()

        return downloader.download(
            video_url=url,
            output_dir=self.output_dir,
        )