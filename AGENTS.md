# AGENTS.md

## Project

- Name: Video2MD
- Purpose: Convert supported online video and account URLs into structured Markdown knowledge.
- Stack: Python 3.13+, SQLite, Whisper, yt-dlp, FFmpeg, Rich, Loguru, PyYAML.

## Working Rules

- Read `ai/DEVELOPMENT.md` and `ai/AI_CONTEXT.md` before implementation.
- Keep the existing architecture; `Application` controls workflows.
- Exchange models, never dictionaries.
- Register each platform parser in the registry; keep platform-specific logic out of the router.
- Use type hints, docstrings, English identifiers, and PEP 8.
- Do not store credentials in this repository.
