# -*- coding: utf-8 -*-


#
# IMPORTS
#


import logging
import os
import random
import string
import sys
import time
from enum import Enum
from itertools import zip_longest
from pathlib import Path
from typing import Any, Iterable, Union

from .config import LoggingLevel

#
#
# TYPES
#


int0 = int  # integer >= 0


#
# CONSTANTS
#


LOGGING_FORMATTER_STR = "%(asctime)sZ - %(name)s - %(levelname)s - %(message)s"


#
# TYPES
#


class Color(str, Enum):
    GRAY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BRIGHT = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


#
# FUNCTIONS
#


def colorize(text: str, color: Color) -> str:
    return color + text + Color.RESET


def gray(text: str) -> str:
    return colorize(text, Color.GRAY)


def red(text: str) -> str:
    return colorize(text, Color.RED)


def green(text: str) -> str:
    return colorize(text, Color.GREEN)


def yellow(text: str) -> str:
    return colorize(text, Color.YELLOW)


def bright(text: str) -> str:
    return colorize(text, Color.BRIGHT)


def underline(text: str) -> str:
    return colorize(text, Color.UNDERLINE)


def print_(s: str, **kwargs: Any) -> None:
    print(s, flush=True, **kwargs)


def create_logger(
    name: str,
    *,
    log_file: Union[str, Path],
    formatter_str: str,
    level: LoggingLevel  # note union
) -> logging.Logger:
    log_file = Path(log_file)
    formatter = logging.Formatter(formatter_str)
    formatter.converter = time.gmtime
    logger = logging.getLogger(name)
    os.makedirs(log_file.parent, exist_ok=True)
    file_log_handler = logging.FileHandler(
        log_file,
        mode="a",
        encoding="utf-8",
        delay=False,
    )
    file_log_handler.setFormatter(formatter)
    logger.addHandler(file_log_handler)
    stdout_log_handler = logging.StreamHandler(stream=sys.stdout)
    stdout_log_handler.setFormatter(formatter)
    logger.addHandler(stdout_log_handler)
    logger.setLevel(level)
    return logger


def get_random_string(length: int0) -> str:
    # choose from all lowercase letters, uppercase letters, and digits
    letters = string.ascii_letters + string.digits
    result_str = "".join(random.choice(letters) for _ in range(length))
    return result_str


def compare_iterables(iterable1: Iterable[Any], iterable2: Iterable[Any]) -> bool:
    """
    Compares pairs of elements of two iterables iteratively to avoid loading
    all elements at once
    """
    sentinel = object()
    return all(
        (a == b and a is not sentinel and b is not sentinel)
        for a, b in zip_longest(iterable1, iterable2, fillvalue=sentinel)
    )
