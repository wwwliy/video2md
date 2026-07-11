"""
Config Loader
"""

from pathlib import Path

import yaml


CONFIG_PATH = Path("config.yaml")


class Config:

    def __init__(self):

        if CONFIG_PATH.exists():

            with open(CONFIG_PATH, "r", encoding="utf-8") as f:

                self.data = yaml.safe_load(f)

        else:

            self.data = {}

    def get(self, *keys, default=None):

        node = self.data

        for key in keys:

            if not isinstance(node, dict):

                return default

            node = node.get(key)

            if node is None:

                return default

        return node