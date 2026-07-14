# Video2MD Development Guide

Version: 1.0

---

# Project Goal

Video2MD is a multi-platform video content extraction system.

Input:

- Video URL
- Account URL

Output:

- Markdown
- Transcript
- Subtitle
- AI Summary
- Knowledge Base

---

# Development Principles

## 1. Single Responsibility

Each module has one responsibility only.

Examples:

Router
    Identify platform and URL type.

Downloader
    Download media only.

Speech
    Convert audio to text.

Markdown
    Generate markdown only.

Database
    Save project data only.

---

## 2. Application is the only workflow controller.

Never let modules call each other directly.

Correct:

Application
    ↓
Router
    ↓
Downloader
    ↓
Speech
    ↓
Markdown

Wrong:

Downloader
    ↓
Speech

---

## 3. Models only

Never exchange dict between modules.

Always use Models.

Examples:

UrlInfo

DownloadTask

DownloadResult

Transcript

MarkdownDocument

---

## 4. Plugin Architecture

Every platform must be implemented as a plugin.

Example:

DouyinParser

TikTokParser

YoutubeParser

No Router modification when adding new platform.

---

## 5. Configuration

Never hardcode configuration.

Everything must come from config.yaml.

---

## 6. Output

Generated files must be stored inside output/.

---

# Coding Style

PEP8

Type Hint required

Docstring required

English identifiers only

Chinese comments are allowed.

---

# Git

Feature Branch only.

Commit examples:

feat(router): add douyin parser

fix(download): retry bug

docs(sprint): update roadmap

refactor(router): simplify registry

---

# Review Checklist

Before commit:

✓ No duplicated code

✓ Type Hint

✓ Logger

✓ Exception handling

✓ Config instead of hardcode

✓ Unit test if possible
