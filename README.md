# ak-tools

## Overview 

1. The repository is intended to serve as a __blueprint__ (or, template) of a [Python](https://www.python.org/) project to allow an easy set up. At the same time, to avoid duplication, it can be used as a blueprint for a [Lean](https://lean-lang.org/) project (these are my preferred languages for programming and math, respectively). To find your way around: Python (resp., Lean) package top-level is `ak_tools/` (resp., `AkTools/`). Note also that part of the material in the repository root folder is redundant if it is used with only *one* of Python or Lean.

1. The repository contains ___setup guides___ for a Python (resp., Lean) development environment (under `docs/`; we value modern and flexible CLI-based tools and strictly adhere to free and open source solutions).

1. The repository includes (system-wide) ___dotfiles___ for [Bash](https://www.gnu.org/software/bash/)-type shells and different free and open source CLI-based utilities (under `users/7766612/dotfiles/`). Dotfiles can be referenced (or copied over) to allow easy setup of new developer machines.

1. The repo includes (still, a few) common tools and utilities in Python and Lean.

Note that the repository blueprint is set to allow multiple "user spaces" (under `users/`). A user space may include a developer's environment files (to be tracked with Git independently of other developers) and secret files too (e.g., authentication keys; not to be tracked).

## List of Contents

1. An integrated project blueprint:

    + [Python](https://www.python.org/) project and configuration files (package top-level at `ak_tools/`)

        - Including [Poetry](https://python-poetry.org/), [Docker](https://www.docker.com/), [Make](https://www.gnu.org/software/make/), [Git](https://git-scm.com/), [DVC](https://dvc.org/), environment files, secrets

    + [Lean](https://lean-lang.org/) project and configuration files (package top-level at `AkTools/`)

        - Including a [mathlib](https://leanprover-community.github.io/mathlib-overview.html) dependency

    + [Jupyter notebooks](https://jupyter.org/) and [Markdown](https://daringfireball.net/projects/markdown/) documents

    + The project is set up to allow multiple *user spaces* under `users/` while the existing user is symlinked with `.user`.

2. Setup guides:

    + A guide on setting up a [Python](https://www.python.org/) development environment in `docs/setting-up-python.md`:

        - Including [pyenv](https://github.com/pyenv/pyenv) (maintaining multiple python versions), [Poetry](https://python-poetry.org/) (a modern dependency manager, virtual environment, and project builder in one), [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) (sharable project templates), [Podman](https://podman.io/) (a free Docker engine as a replacement for Docker Desktop)

    + A short guide on setting up a [Lean](https://lean-lang.org/) development environment with a [mathlib](https://leanprover-community.github.io/mathlib-overview.html) dependency in `docs/setting-up-lean4.md`.

3. System-wide dotfiles in folder `users/7766612/dotfiles/`:

    + Including [Bash](https://www.gnu.org/software/bash/), [tmux](https://github.com/tmux/tmux/wiki), [Vim](https://www.vim.org/), [VS Code](https://code.visualstudio.com/)

4. Toolbox:

    + Python tools and utilities (under `ak_tools/`) -- still, a few

    + Lean tools and utilities (under `AkTools/`) -- to be added
