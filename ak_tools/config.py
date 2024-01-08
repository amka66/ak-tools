# -*- coding: utf-8 -*-


#
# IMPORTS
#


import os
from abc import ABC
from pathlib import Path
from typing import Literal

from platformdirs import user_config_dir, user_log_dir
from pydantic import BaseModel, ConfigDict, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict
from rich import print

from .read import read_toml

#
# TYPE HINTS
#


LoggingLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


#
#
# CONSTANTS
#


_ROOT_DIR = Path(__file__).parent.parent
_pyproject = read_toml(_ROOT_DIR / "pyproject.toml")
_PROJECT_NAME: str = _pyproject["tool"]["poetry"]["name"]
_PACKAGE_NAME = _PROJECT_NAME.replace("-", "_")
_VERSION = _pyproject["tool"]["poetry"]["version"]
_ENV_PREFIX = f"{_PACKAGE_NAME}_"
assert (
    _PACKAGE_NAME == _pyproject["tool"]["poetry"]["packages"][0]["include"]
), "Package name mismatch"

_IS_DEV_ENV = (_ROOT_DIR / ".dev").is_file()
if _IS_DEV_ENV:
    _LOG_DIR = _ROOT_DIR / "logs"
    os.makedirs(_LOG_DIR, exist_ok=True)
    _ENV_DIR = _ROOT_DIR
else:
    _LOG_DIR = Path(user_log_dir(_PROJECT_NAME))
    os.makedirs(_LOG_DIR, exist_ok=True)
    print(f"Logs may be found in {_LOG_DIR}")
    _ENV_DIR = Path(user_config_dir(_PROJECT_NAME))
    os.makedirs(_ENV_DIR, exist_ok=True)
    print(f"Environment files and secrets may be stored in {_ENV_DIR}")


#
# PROJECT INFORMATION
#


class MyBaseInfo(BaseModel, ABC):
    model_config = ConfigDict(
        validate_default=True,
    )


class GeneralInfo(MyBaseInfo):
    root_dir: DirectoryPath = _ROOT_DIR
    project_name: str = _PROJECT_NAME
    package_name: str = _PACKAGE_NAME
    version: str = _VERSION
    is_dev_env: bool = _IS_DEV_ENV
    log_dir: DirectoryPath = _LOG_DIR
    env_dir: DirectoryPath = _ENV_DIR


info = GeneralInfo()


#
# PROJECT SECRETS
#


class MyBaseSecrets(BaseSettings, ABC):
    model_config = SettingsConfigDict(
        env_file=info.env_dir / ".secrets",
        env_file_encoding="utf-8",
        env_prefix=_ENV_PREFIX,
        extra="ignore",
    )


#
# PROJECT SETTINGS
#


class MyBaseSettings(BaseSettings, ABC):
    model_config = SettingsConfigDict(
        env_file=info.env_dir / ".env",
        env_file_encoding="utf-8",
        env_prefix=_ENV_PREFIX,
        extra="ignore",
    )


class GeneralSettings(MyBaseSettings):
    logging_level: LoggingLevel = "WARNING"


settings = GeneralSettings()
