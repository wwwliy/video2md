"""
Project Logger
"""

from pathlib import Path

from loguru import logger


LOG_DIR = Path("logs")

LOG_DIR.mkdir(exist_ok=True)

logger.add(

    LOG_DIR / "video2md.log",

    rotation="10 MB",

    retention=10,

    encoding="utf-8",

)

__all__ = ["logger"]