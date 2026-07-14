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

        # .env 指定的模型（可为空）
        preferred = os.getenv("MODEL")

        default_models = [
            "models/gemini-2.0-flash",
            "models/gemini-3.1-flash-lite",
            "models/gemini-flash-latest",
        ]

        self.models = []

        if preferred:
            self.models.append(preferred)

        for m in default_models:
            if m not in self.models:
                self.models.append(m)

        # 当前成功模型（缓存）
        self._model = self.models[0]

    @property
    def model(self):
        return self._model

    def ask(
        self,
        prompt,
        system_prompt="",
        temperature=0.2,
    ):

        full_prompt = f"""{system_prompt}

----------------------------

{prompt}
"""

        last_error = None

        #
        # 优先使用上一次成功模型
        #
        model_list = [self._model]

        for m in self.models:
            if m not in model_list:
                model_list.append(m)

        #
        # 依次尝试模型
        #
        for model in model_list:

            self._model = model

            print("=" * 60)
            print("[Gemini]")
            print("Model :", model)
            print("Chars :", len(full_prompt))
            print("=" * 60)

            #
            # 每个模型只 Retry 一次
            #
            for retry in range(2):

                try:

                    response = self.client.models.generate_content(

                        model=model,

                        contents=full_prompt,

                        config=types.GenerateContentConfig(
                            temperature=temperature,
                        ),
                    )

                    print("✓ Success\n")

                    # 缓存成功模型
                    self._model = model

                    return response.text.strip()

                except Exception as e:

                    last_error = e

                    msg = str(e)

                    #
                    # Retry 一次
                    #
                    if retry == 0:

                        print()

                        print("Retry 1/1")

                        print(type(e).__name__)

                        print(msg)

                        print("等待 3 秒...")

                        print()

                        time.sleep(3)

                        continue

                    #
                    # Retry 后仍失败
                    #
                    print()

                    print("Model Failed")

                    print(model)

                    print()

                    break

        print("=" * 60)
        print("All Gemini Models Failed")
        print("=" * 60)

        for m in model_list:
            print(m)

        print("=" * 60)

        raise last_error