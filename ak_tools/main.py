import sys

import typer
from rich import print

from . import PROJECT_NAME, __version__

app = typer.Typer()


@app.command()
def command1():
    """Command #1"""
    print("Command #1 started ...")
    print("system", sys.version)
    print("package", __version__)
    print("... command #1 ended")


@app.command()
def command2():
    """Command #2"""
    print("Command #2 started ...")
    print("system", sys.version)
    print("package", __version__)
    print("... command #2 ended")


def main():
    app(prog_name=PROJECT_NAME)
