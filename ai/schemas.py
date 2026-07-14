"""
Shared data models for the AI pipeline.

Video2MD AI Pipeline

Markdown
    ↓
Splitter
    ↓
AI
    ↓
Parser
    ↓
KnowledgeDocument
    ↓
Merger
    ↓
Renderer
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class VideoInfo:
    """
    Video metadata kept in the final knowledge document.
    """

    url: str = ""
    collected_at: str = ""


@dataclass
class KnowledgeDocument:
    """
    Parsed AI result.

    Every AI response will first be converted into this object.
    Multiple KnowledgeDocument objects can then be merged safely.
    """

    title: str = ""

    video_info: VideoInfo = field(default_factory=VideoInfo)

    viewpoints: list[str] = field(default_factory=list)

    keywords: list[str] = field(default_factory=list)

    contents: list[str] = field(default_factory=list)

    quotes: list[str] = field(default_factory=list)


@dataclass
class MergeResult:
    """
    Final merged document before rendering.
    """

    title: str = ""

    video_info: VideoInfo = field(default_factory=VideoInfo)

    viewpoints: list[str] = field(default_factory=list)

    keywords: list[str] = field(default_factory=list)

    contents: list[str] = field(default_factory=list)

    quotes: list[str] = field(default_factory=list)