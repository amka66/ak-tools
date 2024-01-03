from pathlib import Path

import toml

ROOT = Path(__file__).parent.parent
PYPROJECT = toml.load(ROOT / "pyproject.toml")
__version__ = PYPROJECT["tool"]["poetry"]["version"]
PROJECT_NAME = PYPROJECT["tool"]["poetry"]["name"]
