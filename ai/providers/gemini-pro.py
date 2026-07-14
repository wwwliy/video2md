"""
Gemini Provider
"""

import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from .base import BaseProvider

load_dotenv()


class GeminiProvider(BaseProvider):

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("未配置 GEMINI_API_KEY")

        self.client = genai.Client(
            api_key=api_key
        )

        preferred = os.getenv("MODEL")

        default_models = [

            "models/gemini-3.1-flash-lite",

            "models/gemini-2.0-flash",

            "models/gemini-flash-latest",

        ]

        self.models = []

        if preferred:
            self.models.append(preferred)

        for model in default_models:

            if model not in self.models:
                self.models.append(model)

        #
        # 当前正在使用的模型
        #
        self._model = self.models[0]

        #
        # 当前运行期间禁用的模型
        #
        self.disabled_models = set()

    @property
    def model(self):

        return self._model
    
    def ask(
        self,
        prompt,
        system_prompt="",
        temperature=0.3,
    ):

        full_prompt = system_prompt + "\n\n" + prompt

        last_error = None

        #
        # 优先使用最近成功模型
        #
        candidate_models = [self._model]

        for model in self.models:

            if (
                model != self._model
                and model not in self.disabled_models
            ):
                candidate_models.append(model)

        for model in candidate_models:

            print("=" * 60)
            print("[Gemini]")
            print("Model :", model)
            print("Chars :", len(full_prompt))
            print("=" * 60)

            retry = 0

            while retry <= 1:

                try:

                    response = self.client.models.generate_content(

                        model=model,

                        contents=full_prompt,

                        config=types.GenerateContentConfig(
                            temperature=temperature,
                        ),
                    )

                    self._model = model

                    print("✓ Success\n")

                    return response.text.strip()

                except Exception as e:

                    last_error = e

                    error_text = str(e)

                    #
                    # 401 / 403
                    #
                    if (
                        "401" in error_text
                        or "403" in error_text
                    ):
                        raise e

                    #
                    # 404
                    #
                    if (
                        "404" in error_text
                        or "NOT_FOUND" in error_text
                    ):

                        print("\nModel Not Found")
                        print(model)

                        self.disabled_models.add(model)

                        break

                    #
                    # 429
                    #
                    if (
                        "429" in error_text
                        or "RESOURCE_EXHAUSTED" in error_text
                    ):

                        print("\nQuota Exceeded")
                        print(model)

                        self.disabled_models.add(model)

                        break

                    #
                    # 503
                    #
                    if (
                        "503" in error_text
                        or "UNAVAILABLE" in error_text
                    ):

                        if retry >= 1:

                            print("\nModel Busy")
                            print(model)

                            break

                        retry += 1

                        print(
                            f"\nRetry {retry}/1"
                        )

                        print(type(e).__name__)
                        print(error_text)

                        print("等待 3 秒...\n")

                        time.sleep(3)

                        continue    
                    #
                    # 其它异常
                    #
                    if retry >= 1:

                        print("\nUnknown Error")
                        print(type(e).__name__)
                        print(error_text)

                        break

                    retry += 1

                    print(
                        f"\nRetry {retry}/1"
                    )

                    print(type(e).__name__)
                    print(error_text)

                    print("等待 3 秒...\n")

                    time.sleep(3)

                    continue

            #
            # 当前模型失败
            #
            print("\nModel Failed")
            print(model)
            print()

        #
        # 所有模型都失败
        #
        if last_error:
            raise last_error

        raise RuntimeError(
            "没有可用的 Gemini 模型。"
        )