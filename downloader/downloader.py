"""
Video downloader.

Current implementation:

- Douyin
- Public videos

Future:

- TikTok
- YouTube
- Facebook
- Instagram
"""

from pathlib import Path

import yt_dlp

from core.models import UrlInfo


class Downloader:
    """
    Download videos using yt-dlp.
    """

    def __init__(self, output_dir: str = "output/downloads"):

        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(parents=True, exist_ok=True)

    def download(self, info: UrlInfo) -> Path | None:
        """
        Download one video.

        Returns
        -------
        Path | None
            Downloaded file path.
        """

        if info.url_type != "video":
            print("Only video URL can be downloaded.")
            return None

        output_template = str(
            self.output_dir / f"{info.resource_id}.%(ext)s"
        )

        options = {
            "outtmpl": output_template,
            "quiet": False,
            "noplaylist": True,
            "merge_output_format": "mp4",
            "cookiefile": "cookies.txt",
        }

        try:

            with yt_dlp.YoutubeDL(options) as ydl:

                ydl.download([info.original_url])

        except Exception as e:

            print(f"\nDownload failed:\n{e}")

            return None

        for file in self.output_dir.iterdir():

            if file.stem == info.resource_id:

                return file

        return None
    