import sys

import toml
import typer
from rich import print

from . import __version__ as package_version
from .root import ROOT

app = typer.Typer()


@app.command()
def command1():
    """Command #1"""
    print("Command #1 started ...")
    print("system", sys.version)
    print("package", package_version)
    print("... command #1 ended")


@app.command()
def command2():
    """Command #2"""
    print("Command #2 started ...")
    print("system", sys.version)
    print("package", package_version)
    print("... command #2 ended")


def main():
    app(prog_name=toml.load(ROOT / "pyproject.toml")["tool"]["poetry"]["name"])
