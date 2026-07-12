"""
Application workflow controller.
"""

import argparse
from collections.abc import Sequence

from core.router import Router
from downloader.downloader import Downloader
from input.manager import InputManager


class Application:
    """
    Main application workflow.
    """

    def __init__(self) -> None:

        self.router = Router()
        self.input_manager = InputManager()
        self.downloader = Downloader()

    def run(self, arguments: Sequence[str] | None = None) -> None:

        parser = argparse.ArgumentParser(
            description="Video2MD"
        )

        parser.add_argument(
            "source",
            help="Video URL or local video file."
        )

        args = parser.parse_args(arguments)

        source = args.source

        # -----------------------------------
        # Local Video
        # -----------------------------------

        if self.input_manager.is_local(source):

            video_path = self.input_manager.load_local(source)

            print("Input Type : local")
            print(f"Video      : {video_path}")
            print("------------------------------------")

            # Feature3 Whisper 将从这里开始
            return

        # -----------------------------------
        # URL
        # -----------------------------------

        if self.input_manager.is_url(source):

            info = self.router.parse(source)

            print(f"Platform : {info.platform}")
            print(f"Type     : {info.url_type}")
            print(f"ID       : {info.resource_id}")
            print("------------------------------------")

            if info.url_type == "video":

                print("Downloading...\n")

                video = self.downloader.download(info)

                if video:

                    print("\nDownload Success.")
                    print(video)

                else:

                    print("\nDownload failed.")

            return

        # -----------------------------------
        # Invalid Input
        # -----------------------------------

        print("Unsupported input.")