# ak-tools

The repository includes an integrated **Python / Lean4 project template** and **toolbox**, system-wide **dotfiles**, and opinionated **setup guides**. Each can be borrowed and used independently.

- Integrated project template:

    + Python project and configuration files

        - Including poetry, docker, make, git, dvc, dotenv files, secrets

    + Lean4 project and configuration files (extending the python project and vice versa)

        - Including a mathlib4 dependency

    + Jupyter notebooks and Markdown documents

    + The project is set up to allow *personal user spaces*

- Toolbox:

    + Python tools (only a few; TBA)

    + Lean4 tools (TBA)

- System-wide dotfiles in folder `users/7766612/dotfiles/`:

    + Including bash, tmux, vim, vscode

- Setup guides:

    + A guide on setting up a python development environment in `docs/setting-up-python.md`:

        - Including pyenv (easily installing multiple / new python versions), poetry (a modern dependency manager, virtual environment, and project builder in one), cookiecutter (sharable project templates), podman docker engine (a free replacement to docker desktop)

    + A short guide on setting up a lean4 development environment with mathlib4 dependency in `docs/setting-up-lean4.md`.
