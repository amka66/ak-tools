# -*- coding: utf-8 -*-


#
# IMPORTS
#


import asyncio
import sys

import typer
from rich import print

from .config import GeneralSettings, info
from .gpt import call_gpt
from .utils import LOGGING_FORMATTER_STR, create_logger

#
#
# CONFIGURATION
#


class MainSettings(GeneralSettings):
    main_model: str
    main_content: str


#
# INITIALIZATION
#


settings = MainSettings()

app = typer.Typer()

logger = create_logger(
    __name__,
    log_file=info.log_dir / f"{__name__}.log",
    formatter_str=LOGGING_FORMATTER_STR,
    level=settings.logging_level,
)


#
# COMMANDS
#


async def do_command() -> None:
    print("system", sys.version)
    print("package", info.version)
    print(settings.main_content)
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": settings.main_content,
        },
    ]
    _, message, response = await call_gpt(messages, model=settings.main_model)
    print(message.content)
    logger.info(
        "system %s - package %s - model %s",
        sys.version,
        info.version,
        response.model,
    )


@app.command()
def command1() -> None:
    """Command #1"""
    print("Command #1 started ...")
    asyncio.run(do_command())
    print("... command #1 ended")


@app.command()
def command2() -> None:
    """Command #2"""
    print("Command #2 started ...")
    asyncio.run(do_command())
    print("... command #2 ended")


#
# MAIN
#


def main() -> None:
    app(prog_name=info.project_name)
