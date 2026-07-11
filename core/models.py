"""
Project Models

所有模块之间统一使用 Model。

禁止返回 dict。

"""


from dataclasses import dataclass
from typing import Literal


Platform = Literal[
    "douyin",
    "tiktok",
    "youtube",
    "unknown",
]


UrlType = Literal[
    "video",
    "account",
    "unknown",
]


@dataclass(slots=True)
class UrlInfo:

    platform: Platform

    url_type: UrlType

    original_url: str

    resource_id: str | None = None