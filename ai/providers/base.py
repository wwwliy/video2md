"""
AI Provider Base Class

所有 AI Provider 必须继承该类。
"""

from abc import ABC
from abc import abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def ask(
        self,
        prompt: str,
        system_prompt: str = "",
        temperature: float = 0.3,
    ) -> str:
        """
        调用大模型。

        Args:
            prompt: 用户输入
            system_prompt: 系统提示词
            temperature: 随机性

        Returns:
            str
        """
        raise NotImplementedError

    @property
    def model(self) -> str:
        """
        当前模型名称。
        """
        return "unknown"

    def __repr__(self):
        return f"<{self.__class__.__name__} model={self.model}>"