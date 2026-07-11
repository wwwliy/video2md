"""
Platform Parser Base Class
"""

from abc import ABC, abstractmethod

from core.models import UrlInfo


class PlatformParser(ABC):

    @property
    @abstractmethod
    def platform_name(self) -> str:
        """
        平台名称
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def domains(self) -> list[str]:
        """
        支持的域名
        """
        raise NotImplementedError

    @abstractmethod
    def parse(self, url: str) -> UrlInfo:
        """
        解析URL
        """
        raise NotImplementedError