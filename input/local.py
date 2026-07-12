"""
Local video input.
"""

from pathlib import Path


class LocalInput:
    """
    Handle local video files.
    """

    VIDEO_EXTENSIONS = {
        ".mp4",
        ".mov",
        ".avi",
        ".mkv",
        ".flv",
        ".webm",
    }

    def can_handle(self, source: str) -> bool:
        """
        Check whether the input is a local video.
        """

        path = Path(source)

        return (
            path.exists()
            and path.is_file()
            and path.suffix.lower() in self.VIDEO_EXTENSIONS
        )

    def load(self, source: str) -> Path:
        """
        Return local video path.
        """

        return Path(source).resolve()