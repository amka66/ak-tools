# -*- coding: utf-8 -*-


"""
Functions for reading all sorts of data files.

All functions must conform to the type `Callable[[Path], Any]`,
possibly including more parameters (and possibly a specialization
of this type).
"""


#
# IMPORTS
#


import json
import pickle
from pathlib import Path
from typing import Any, List

import jsonlines
import jsonpickle
import numpy as np
import pandas as pd
import yaml

#
#
# READ FUNCTIONS
#


# *.txt
def read_text(file: Path) -> str:
    with open(file, "r", encoding="utf-8") as f_d:
        return f_d.read()


# *.txtl
def read_lines(file: Path) -> List[str]:
    with open(file, "r", encoding="utf-8") as f_d:
        return [line.rstrip("\n") for line in f_d]


# *.json
def read_json(file: Path) -> Any:
    with open(file, "r", encoding="utf-8") as f_d:
        return json.load(f_d)


# *.yaml
def read_yaml(file: Path, **kwargs: Any) -> Any:
    with open(file, "r", encoding="utf-8") as f_d:
        return yaml.safe_load(f_d, **kwargs)


# *.jsonl
def read_jsonlines(file: Path) -> List[Any]:
    with jsonlines.open(file, "r") as f_reader:
        return [obj for obj in f_reader]


# *.df.jsonl
def read_jsonlines_to_dataframe(file: Path) -> pd.DataFrame:
    return pd.read_json(file, orient="records", lines=True, encoding="utf-8")


# *.csv
def read_csv(
    file: Path, *, sep: str = ",", index_col=None, **kwargs: Any
) -> pd.DataFrame:
    return pd.read_csv(file, encoding="utf-8", sep=sep, index_col=index_col, **kwargs)


# *.tsv
def read_tsv(file: Path, **kwargs: Any) -> pd.DataFrame:
    return read_csv(file, sep="\t", **kwargs)


# *.int64.nptxt
def read_nptxt_int64(
    file: Path,
) -> np.ndarray[np.dtype[np.int64], np.dtype[np.int64]]:
    return np.loadtxt(file, dtype=np.int64, encoding="utf-8")


# *.float64.nptxt
def read_nptxt_float64(
    file: Path,
) -> np.ndarray[np.dtype[np.float64], np.dtype[np.float64]]:
    return np.loadtxt(file, dtype=np.float64, encoding="utf-8")


# *.pickle
def read_pickle(file: Path) -> Any:
    """Generally unsafe!"""
    with open(file, "br") as f_d:
        return pickle.load(f_d)


# *.pickle.json
def read_jsonpickle(file: Path, **kwargs: Any) -> Any:
    """Generally unsafe!"""
    # return jsonpickle.decode(read_text(file), **kwargs)
    unpickler = jsonpickle.unpickler.Unpickler(**kwargs)
    return unpickler.restore(read_json(file))


# *.pickle.jsonl
def read_jsonlinespickle(file: Path, **kwargs: Any) -> List[Any]:
    """Generally unsafe!"""
    # def decode(encoded: str) -> Any:
    #     return jsonpickle.decode(encoded, **kwargs)
    # return list(map(decode, read_lines(file)))
    unpickler = jsonpickle.unpickler.Unpickler(**kwargs)
    return list(map(unpickler.restore, read_jsonlines(file)))
