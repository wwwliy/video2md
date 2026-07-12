from pathlib import Path
import json
import time

import requests
from playwright.sync_api import sync_playwright

from downloader.platform_detector import get_greenvideo_page


class GreenVideoDownloader:

    def __init__(self):
        self.download_url = None

    def _on_response(self, response):

        if "getDownloadInfo" not in response.url:
            return

        try:

            data = response.json()

            print("\n========== getDownloadInfo ==========")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            print("=====================================\n")

            if (
                data.get("success")
                and data.get("data")
                and data["data"].get("downloadUrl")
            ):

                self.download_url = data["data"]["downloadUrl"]

                print("✔ 获取真实下载地址成功")

        except Exception as e:
            print(e)

    def download(
        self,
        video_url: str,
        output_dir="downloads",
    ):

        self.download_url = None

        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True, parents=True)

        save_path = output_dir / f"{int(time.time())}.mp4"

        target_page = get_greenvideo_page(video_url)

        print(f"\n平台页面：{target_page}\n")

        with sync_playwright() as p:

            browser = p.chromium.launch(
                channel="chrome",
                headless=False,
                slow_mo=300,
            )

            page = browser.new_page()

            page.on(
                "response",
                self._on_response,
            )

            page.goto(
                target_page,
                wait_until="networkidle",
            )

            page.get_by_role(
                "textbox",
                name="请将复制的视频链接粘贴到此处，并点击开始按钮",
            ).fill(video_url)

            page.get_by_role(
                "button",
                name="开始",
            ).click()

            print("等待解析...")

            download_btn = page.get_by_role(
                "button",
                name="下载",
                exact=True,
            )

            download_btn.wait_for(timeout=30000)

            download_btn.click()

            timeout = 20

            while self.download_url is None and timeout > 0:

                page.wait_for_timeout(1000)

                timeout -= 1

            browser.close()

        if self.download_url is None:
            raise RuntimeError("没有获取到真实下载地址")

        print("\n开始下载视频...\n")

        with requests.get(
            self.download_url,
            stream=True,
            timeout=120,
        ) as r:

            r.raise_for_status()

            with open(save_path, "wb") as f:

                for chunk in r.iter_content(1024 * 1024):

                    if chunk:
                        f.write(chunk)

        print(f"✔ 下载完成：{save_path}")

        return save_path


if __name__ == "__main__":

    url = "https://www.douyin.com/video/7660952849539547249"

    downloader = GreenVideoDownloader()

    video = downloader.download(url)

    print(video)