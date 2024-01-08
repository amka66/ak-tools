# -*- coding: utf-8 -*-


"""
Functions for writing all sorts of data files.

All functions must return a function to read the newly written file,
after optionally verifying that it indeed returns the proper (equal) object.
The returned function must conform to the type `Callable[[Path], Any]`,
possibly including more parameters (and possibly a specialization
of this type).
"""


#
# IMPORTS
#


import json
import pickle
from pathlib import Path
from typing import Any, Callable, Iterable, List

import jsonlines
import jsonpickle
import pandas as pd

from .read import (
    read_json,
    read_jsonlines,
    read_jsonlines_to_dataframe,
    read_jsonlinespickle,
    read_jsonpickle,
    read_lines,
    read_pickle,
    read_text,
)
from .utils import compare_iterables

#
#
# WRITE FUNCTIONS
#


class ReadVerificationError(IOError):
    """
    Raised when the verification of the corresponding read operation
    on the newly created data fails
    """


# *.txt
def write_text(
    text: str, file_out: Path, verify: bool = False
) -> Callable[[Path], str]:
    """Write text string to file and optionally verify read operation"""
    with open(file_out, "w", encoding="utf-8") as f_d:
        f_d.write(text)
    if verify and read_text(file_out) != text:
        raise ReadVerificationError
    return read_text


# *.txtl
def write_lines(
    lines: Iterable[str], file_out: Path, verify: bool = False
) -> Callable[[Path], List[str]]:
    """Write text lines to file and optionally verify read operation"""
    with open(file_out, "w", encoding="utf-8") as f_d:
        for line in lines:
            f_d.write(line)
            f_d.write("\n")
    if verify and not compare_iterables(read_lines(file_out), lines):
        raise ReadVerificationError
    return read_lines


# *.json
def write_json(
    obj_compatible: Any, file_out: Path, verify: bool = False
) -> Callable[[Path], Any]:
    """Write json to file and optionally verify read operation"""
    with open(file_out, "w", encoding="utf-8") as f_d:
        json.dump(obj_compatible, f_d)
    if verify and read_json(file_out) != obj_compatible:
        raise ReadVerificationError
    return read_json


# *.jsonl
def write_jsonlines(
    objs_compatible: Iterable[Any], file_out: Path, verify: bool = False
) -> Callable[[Path], List[Any]]:
    """Write jsonlines to file and optionally verify read operation"""
    with jsonlines.open(file_out, "w") as f_d:
        f_d.write_all(objs_compatible)
    if verify and not compare_iterables(read_jsonlines(file_out), objs_compatible):
        raise ReadVerificationError
    return read_jsonlines


# *.df.jsonl
def write_dataframe_to_jsonlines(
    df: pd.DataFrame, file_out: Path, verify: bool = False
) -> Callable[[Path], pd.DataFrame]:
    """Write dataframe to jsonlines file and optionally verify read operation"""
    df.to_json(file_out, orient="records", lines=True)
    if verify and not read_jsonlines_to_dataframe(file_out).equals(df):
        raise ReadVerificationError
    return read_jsonlines_to_dataframe


# *.pickle
def write_pickle(
    obj: Any, file_out: Path, verify: bool = False
) -> Callable[[Path], Any]:
    """Write object to pickle file and optionally verify read operation"""
    with open(file_out, "wb") as f_d:
        pickle.dump(obj, f_d)
    if verify and read_pickle(file_out) != obj:
        raise ReadVerificationError
    return read_pickle


# *.pickle.json
def write_jsonpickle(
    obj: Any,
    file_out: Path,
    verify: bool = False,
    **kwargs: Any,
) -> Callable[[Path], Any]:
    """Write object to json and optionally verify read operation"""
    # write_text(jsonpickle.encode(obj, **kwargs), verify=False)
    pickler = jsonpickle.pickler.Pickler(**kwargs)
    write_json(pickler.flatten(obj), file_out, verify=False)
    if verify and read_jsonpickle(file_out) != obj:
        raise ReadVerificationError
    return read_jsonpickle


# *.pickle.jsonl
def write_jsonlinespickle(
    objs: Iterable[Any],
    file_out: Path,
    verify: bool = False,
    **kwargs: Any,
) -> Callable[[Path], List[Any]]:
    """Write a list of objects to json and optionally verify read operation"""
    # def encode(obj: Any) -> str:
    #     return jsonpickle.encode(obj, **kwargs)
    # write_lines(map(encode, objs), file_out, verify=False)
    pickler = jsonpickle.pickler.Pickler(**kwargs)
    write_jsonlines(map(pickler.flatten, objs), file_out, verify=False)
    if verify and not compare_iterables(read_jsonlinespickle(file_out), objs):
        raise ReadVerificationError
    return read_jsonlinespickle
