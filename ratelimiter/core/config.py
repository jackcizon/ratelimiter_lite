import os
import json
from pathlib import Path
from typing import Literal, cast

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ratelimiter_DIR = os.path.join(ROOT_DIR, "ratelimiter")

ENVS_DIR = os.path.join(ROOT_DIR, "envs")
ENV_FLAG = os.getenv("ENV", "dev")  # register into os envs, default is dev


class Settings:  # pragma: no cover
    """app settings"""

    @staticmethod
    def _load(env_flag: Literal["dev", "test", "prod"]) -> dict:
        config_path = os.path.join(ENVS_DIR, f"config.{env_flag}.json")  # read config dynamically
        with open(config_path, mode="rt", encoding="utf-8") as fp:
            return json.load(fp=fp)

    def __init__(
        self, env_flag: Literal["dev", "test", "prod"] = cast(Literal["dev", "test", "prod"], ENV_FLAG)
    ) -> None:
        self.config_dict = self._load(env_flag)
        # basic
        self.env: str = self.config_dict["env"]
        self.debug: bool = self.config_dict["debug"]


# use module level singleton
settings = Settings()
