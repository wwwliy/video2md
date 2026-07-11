"""
Douyin Parser
"""

import re

from core.models import UrlInfo
from platforms.base import PlatformParser


class DouyinParser(PlatformParser):
    """Parse Douyin video and account URLs."""

    VIDEO_PATTERN = re.compile(r"/video/(\d+)")

    USER_PATTERN = re.compile(r"/user/([^/?]+)")

    @property
    def platform_name(self) -> str:
        """Return the Douyin platform name."""
        return "douyin"

    @property
    def domains(self) -> list[str]:
        """Return supported Douyin hosts."""
        return [
            "www.douyin.com",
            "douyin.com",
            "v.douyin.com",
        ]

    def parse(self, url: str) -> UrlInfo:
        """Return parsed information or an unknown Douyin URL model."""
        video = self.VIDEO_PATTERN.search(url)
        if video is not None:
            return UrlInfo(
                platform="douyin",
                url_type="video",
                original_url=url,
                resource_id=video.group(1),
            )

        account = self.USER_PATTERN.search(url)
        if account is not None:
            return UrlInfo(
                platform="douyin",
                url_type="account",
                original_url=url,
                resource_id=account.group(1),
            )

        return UrlInfo(
            platform="douyin",
            url_type="unknown",
            original_url=url,
        )
