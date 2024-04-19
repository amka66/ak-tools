# ak-tools

## Overview 

- Firstly, the repository is intended as a *blueprint* (or, template) of a ___Python project___ for a repeatable and easy set up (package top-level at `ak_tools/`). At the same time, to avoid duplication, it can be used as a blueprint for a ___Lean4 project___ (package top-level at `AkTools/`). These are my favorite modern alternatives for programming and reasoning. Part of the material in the repository root folder is redundant if only used for *one* of Python or Lean4.

- Secondly, the repository contains ___setup guides___ (under `docs/`) for Python and Lean development environments, using a modern, effective, free and open source toolset.

- Thirdly, the repository includes system-wide ___dotfiles___ (under `users/7766612/dotfiles/`) for Bash-type shells and other popular, free and open source CLI utilities. These can be referenced (or copied over) for a repeatable and easy set up of the machine.

- Fourth, the repo include (still, a few) common ___tools and utilities___ in Python and Lean4.

- The repository is set up to allow ___multiple user spaces___ (under `users/`), each with different environment files and secret (authentication) files, while the former are being tracked in Git.

## List of Contents

1. An integrated project blueprint:

    + **Python** project (package top-level at `ak_tools/`) and configuration files

        - Including **Poetry**, **Docker**, **Make**, **Git**, **DVC**, environment files, secrets

    + **Lean4** project (package top-level at `AkTools/`) and configuration files

        - Including a **mathlib4** dependency

    + **Jupyter** notebooks and **Markdown** documents

    + The project is set up to allow multiple *user spaces* (under `users/`) while the existing user is symlinked with `.user`.

2. Setup guides:

    + A guide on setting up a Python development environment in `docs/setting-up-python.md`:

        - Including **pyenv** (maintaining multiple python versions), **Poetry** (a modern dependency manager, virtual environment, and project builder in one), **Cookiecutter** (sharable project templates), **Podman** (a free Docker engine as a replacement for Docker Desktop)

    + A short guide on setting up a Lean4 development environment with mathlib4 dependency in `docs/setting-up-lean4.md`.

3. System-wide dotfiles in folder `users/7766612/dotfiles/`:

    + Including **Bash**, **tmux**, **Vim**, **VS Code**

4. Toolbox:

    + Python tools and utilities (under `ak_tools/`) -- still, a few

    + Lean4 tools and utilities (under `AkTools/`) -- to be added
