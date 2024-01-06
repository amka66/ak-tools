# Setting up a Python development environment on Mac and Linux

Author: Amir Kantor  
Updated: December 2023

## Part 1 -- Setting up Python (pyenv, poetry, cookiecutter)

Source:
[How to manage multiple Python versions and virtual environments](https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/) by Dominic Fraser.

### 1.1 pyenv

Needed for using multiple / different versions of python.

First, better to deactivate conda or any other virtual environment management tool (worked for me regardless, but installation outcomes were a bit confusing at first).

For Windows use [pyenv for Windows (pyenv-win)](https://github.com/pyenv-win/pyenv-win) instead.
In other platforms continue with pyenv.

#### 1.1.1 Get pyenv

Source:
- [pyenv Installation](https://github.com/pyenv/pyenv#installation)

##### On linux:

On linux, clone pyenv repo:
```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

On linux, optionally, try to compile dynamic Bash extension for better performance (may fail and that's fine):
```
cd ~/.pyenv && src/configure && make -C src
```

##### On MacOS:

Make sure you have [Homebrew](https://brew.sh/) installed and then:
```
brew update
brew install pyenv
```

#### 1.1.2 Set up shell environment for pyenv

Source:
- [Set up your shell environment for pyenv](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv)

On both linux and macos, for Bash, run the following to modify `~/.profile`, `~/.bash_profile`, or `~/.bash_login` (the one(s) that exists; seems it's *not* needed for `.bashrc`):
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.profile
```

Restart *login* shell for changes to take effect.

Make sure pyenv is properly configured so that python command(s) point to `~/.pyenv/shims/...`:
```
which python
which python3
```

#### 1.1.3 Install python build dependencies for pyenv

Source:
- [suggested build environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)

##### On Ubuntu/Debian:
```
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

If dependecy errors occur, consider the following and repeat (worked for me):
```
sudo apt-get --fix-broken install
```

##### On MacOS:

Make sure you have [Homebrew](https://brew.sh/) installed, as well as Xcode CLI Tools (usually preinstalled during homebrew installation; otherwise install with `xcode-select --install`).

Then:
```
brew install openssl readline sqlite3 xz zlib tcl-tk
```

#### 1.1.4 In the future -- update pyenv

##### On linux:

```
cd ~/.pyenv
git pull
```

##### On MacOS:

```
brew update
brew upgrade pyenv
```

### 1.2 Create a global python version with pyenv

Install a recent python version. If the most recent official python release is 3.x.y, best to take the last update (z) of the previous minor version 3.(x-1).z. For example, if the last python version is 3.11.6, take 3.10.13:
```
pyenv install 3.10.13
```

On macos homebrew installation, if there is an error building python mentioning the C compiler -- repeat after removing xcode cli and reinstalling it with sudo (see [here](https://stackoverflow.com/questions/65778888/pyenv-configure-error-c-compiler-cannot-create-executables)):
```
sudo rm -rf /Library/Developer/CommandLineTools
sudo xcode-select --install
```

Set it as the global version:
```
pyenv global 3.10.13
```

Make sure it is selected via:
```
pyenv versions
```

### 1.3 Install poetry (pip + setuptools replacement)

We will now install poetry as a pip replacement. In contrast to pip, it will install poetry isolated from your python environment.
Make sure `python3` points to the global python version installed with pyenv.

Source:
[poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer)

On Linux / MacOS:
```
curl -sSL https://install.python-poetry.org | python3 -
```

Path to `$HOME/.poetry/bin` is automatically added and set in the login startup script.

For Bash completions run:
```
poetry completions bash >> ~/.bash_completion
```

Restart *login* shell for changes to take effect.

#### 1.3.1 In the future -- update poetry

```
poetry self update
```

### 1.4 Example #1: create a base environment with poetry (optional)

Create a default "base" environment, e.g., for python-based utilities:
```
cd ~/l/projects
poetry new base
cd base
pyenv local 3.10.13
poetry env use 3.10.13
```

Note that `pyenv local 3.10.13` creates a `.python-version` file for documentation and to safeguard the system python: a pyenv interpreter and virtual environment would be activated when poetry is not used (instead of the system python).

Make sure a virtual environment is created and appears as default:
```
poetry env info
```

To activate the base environment in a sub-shell at the base dir:
```
cd ~/l/projects/base
poetry shell
```

Or, to activate in the same shell at the base dir:
```
cd ~/l/projects/base
. $(poetry env info --path)/bin/activate
```

Make sure it is activated by:
```
echo "$VIRTUAL_ENV"
```

To deactivate run:
```
deactivate
```

### 1.5 Example #2: create a data science project with poetry and cookiecutter (optional)

Source:
[How to Structure a Data Science Project for Readability and Transparency](https://towardsdatascience.com/how-to-structure-a-data-science-project-for-readability-and-transparency-360c6716800) by Khuyen Tran.

### 2.1 Cookiecutter template

It will create folder and file hierarchy from a specified data science template.

Install cookiecutter in the base environment:
```
cd ~/l/projects/base
poetry add cookiecutter
```

And activate the base env:
```
poetry shell
```

In the containing dir of your project run:
```
cookiecutter https://github.com/khuyentran1401/data-science-template
```
and answer questions (project name {project-dir} and dir, your name, and ^{minimal-python-version}).
A project dir is created.

Create a default venv for the project:
```
cd {project-dir}
pyenv install 3.x.z  # if not present
pyenv local 3.x.z  # documents the used python version and may be necessary for poetry to install the required version
poetry env use 3.x.z
```

Verify that it is created and appears as default:
```
poetry env info
```

It can be (de)activated as above.
But generally, for working via poetry, it doesn't need to be activated.

Install all dependencies from `pyproject.toml`:
```
poetry install
```

## Part 2 -- Setting up a Docker Engine (podman)

### On MacOS

#### Podman

Due to licensing limitations of Docker Desktop, for a Docker Engine, I use the daemonless and open-source [podman](https://podman.io/docs/installation#macos). It is easily installed via homebrew:

```
brew update
brew install podman
```

Then, create and start your first Podman machine (VM):
```
podman machine init
podman machine start
```

Upon start, seek for a message such as the following and do as instructed:
```
The system helper service is not installed; the default Docker API socket
address can't be used by podman. If you would like to install it run the
following commands:

	sudo <path>/podman-mac-helper install
	podman machine stop; podman machine start
```

You can then verify the installation information using:
```
podman info
```

To stop the Podman machine:
```
podman machine stop
```

#### Docker CLI and Docker Compose CLI

To use the `docker` command, install docker and docker-compose via homebrew:
```
brew update
brew install docker docker-compose
```

Do not confuse it with Docker Desktop installed via cask (`brew install --cask docker`).

#### In the future -- update podman, docker, docker-compose

```
brew update
brew upgrade podman docker docker-compose
```

Copyright (c) 2022-2023 Amir Kantor. All rights reserved.
