video2md/

│
├── app.py                  # 唯一入口（以后不改）
│
├── config.yaml             # 全局配置
├── requirements.txt
├── README.md
├── .gitignore
│
├── core/
│   ├── __init__.py
│   ├── application.py      # 整个流程调度器
│   ├── router.py           # URL识别
│   ├── models.py           # 全部Model
│   ├── config.py           # 配置读取
│   ├── logger.py           # 日志
│   └── exceptions.py
│
├── platforms/
│   ├── __init__.py
│   ├── registry.py         # 平台注册中心
│   ├── base.py
│   ├── douyin.py
│   ├── youtube.py
│   └── tiktok.py
│
├── downloader/
│   ├── __init__.py
│   ├── base.py
│   └── douyin.py
│
├── speech/
│   ├── __init__.py
│   ├── whisper.py
│   └── transcript.py
│
├── markdown/
│   ├── __init__.py
│   └── writer.py
│
├── database/
│   ├── __init__.py
│   └── sqlite.py
│
├── output/
│
├── docs/
│
└── tests/