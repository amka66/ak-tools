# -*- coding: utf-8 -*-


#
# IMPORTS
#


from abc import ABC
from pathlib import Path
from typing import Literal

import toml
from pydantic import DirectoryPath, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

#
# TYPE HINTS
#


LoggingLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


#
#
# CONSTANTS
#


ROOT_DIR = Path(__file__).parent.parent
pyproject = toml.load(ROOT_DIR / "pyproject.toml")
PROJECT_NAME: str = pyproject["tool"]["poetry"]["name"]
PACKAGE_NAME = PROJECT_NAME.replace("-", "_")
ENV_PREFIX = f"{PACKAGE_NAME}_"


#
# BASE TYPES
#


class MyBaseSecrets(BaseSettings, ABC):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".secrets",
        env_file_encoding="utf-8",
        env_prefix=ENV_PREFIX,
        extra="ignore",
    )


class MyBaseSettings(BaseSettings, ABC):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        env_prefix=ENV_PREFIX,
        extra="ignore",
    )


#
#
# TYPES
#


class GeneralSettings(MyBaseSettings):
    root_dir: DirectoryPath = ROOT_DIR
    project_name: str = PROJECT_NAME
    package_name: str = PACKAGE_NAME
    version: str = pyproject["tool"]["poetry"]["version"]

    logging_level: LoggingLevel

    @field_validator("package_name")
    @classmethod
    def check_package(cls, v: str) -> str:
        if isinstance(v, str):
            try:
                assert v == pyproject["tool"]["poetry"]["packages"][0]["include"]
            except Exception:
                raise AssertionError(f"{v} is not the package name in pyproject.toml")
        return v
