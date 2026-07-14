# AI Context

Read this file before generating any code.

---

# Product

Project Name:

Video2MD

Purpose:

Convert online videos into structured Markdown knowledge.

---

# Tech Stack

Python 3.13+

SQLite

Whisper

yt-dlp

FFmpeg

Rich

Loguru

PyYAML

---

# Architecture

Application

↓

Router

↓

Downloader

↓

Speech

↓

Markdown

↓

Database

Application controls everything.

---

# Folder Structure

core/

platforms/

downloader/

speech/

markdown/

database/

output/

docs/

tests/

---

# Rules

Never return dict.

Always return Models.

Never modify Router when adding platform.

Always register platform in Registry.

No business logic inside app.py.

No hardcoded paths.

Use logger.

Use config.yaml.

---

# Naming

PascalCase

Class

snake_case

Functions

UPPER_CASE

Constants

---

# Future Features

TikTok

YouTube

Facebook

Instagram

Batch Download

GUI

REST API

AI Summary

Knowledge Base

RAG

---

# Priority

Correctness

Maintainability

Readability

Performance
