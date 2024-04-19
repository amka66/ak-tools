# ak-tools

## Overview 

- Firstly, the repository is intended as a ___blueprint___ (or, template) of a [Python](https://www.python.org/) project for a repeatable and easy set up. At the same time, to avoid duplication, it can be used as a blueprint for a [Lean](https://lean-lang.org/) project. These are my favorite modern alternatives for programming and reasoning. Package top-levels are at `ak_tools/` and `AkTools/`, respectively, and part of the material in the repository root is redundant if only used for *one* of Python or Lean.

- Secondly, the repository contains ___setup guides___ (under `docs/`) for Python and Lean development environments, using a modern, effective, free and open source toolset.

- Thirdly, the repository includes system-wide ___dotfiles___ (under `users/7766612/dotfiles/`) for [Bash](https://www.gnu.org/software/bash/)-type shells and other popular, free and open source CLI utilities. These can be referenced (or copied over) for a repeatable and easy set up of the machine.

- Fourth, the repo include (still, a few) common ___tools and utilities___ in Python and Lean.

- The repository is set up to allow ___multiple user spaces___ (under `users/`), each with different environment files and secret (authentication) files, while the former are being tracked in Git.

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
