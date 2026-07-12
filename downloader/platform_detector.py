from urllib.parse import urlparse


PLATFORM_MAP = {
    # Douyin
    "douyin.com": "douyin",
    "iesdouyin.com": "douyin",
    "v.douyin.com": "douyin",

    # Xiaohongshu
    "xiaohongshu.com": "xiaohongshu",
    "www.xiaohongshu.com": "xiaohongshu",
    "xhslink.com": "xiaohongshu",

    # Kuaishou
    "kuaishou.com": "kuaishou",
    "www.kuaishou.com": "kuaishou",
    "gifshow.com": "kuaishou",

    # TikTok
    "tiktok.com": "tiktok",
    "www.tiktok.com": "tiktok",
    "vm.tiktok.com": "tiktok",
    "vt.tiktok.com": "tiktok",

    # Instagram
    "instagram.com": "ins",
    "www.instagram.com": "ins",

    # YouTube
    "youtube.com": "youtube",
    "www.youtube.com": "youtube",
    "youtu.be": "youtube",

    # Facebook
    "facebook.com": "fb",
    "www.facebook.com": "fb",
    "fb.watch": "fb",

    # Twitter / X
    "twitter.com": "twitter",
    "www.twitter.com": "twitter",
    "x.com": "twitter",

    # Bilibili
    "bilibili.com": "bilibili",
    "www.bilibili.com": "bilibili",
    "b23.tv": "bilibili",
}


def get_greenvideo_page(video_url: str) -> str:
    """
    根据视频链接返回对应 GreenVideo 页面
    """

    host = urlparse(video_url).netloc.lower()

    for domain, page in PLATFORM_MAP.items():
        if domain in host:
            return f"https://greenvideo.cc/{page}"

    raise ValueError(f"暂不支持的平台：{host}")