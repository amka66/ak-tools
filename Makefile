MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

.PHONY: pull check_no_venv venv check_venv install clean status first recent test push update shell runl build rund brun rbrun
.EXPORT_ALL_VARIABLES:
# .DELETE_ON_ERROR:
# .INTERMEDIATE:
# .SECONDARY:
.DEFAULT_GOAL := status

SYNC ?= --sync

PROJECT_NAME = $(shell poetry version | cut -d' ' -f1)
PACKAGE_NAME = $(shell poetry version | cut -d' ' -f1 | tr '-' '_')
PROJECT_VERSION = $(shell poetry version | cut -d' ' -f2)
PYTHON_VERSION = $(shell cat .python-version)

pull:
	@echo "Pulling file changes..."
	git fetch --all --tags
	[[ -z  "$$(git branch --format "%(upstream:short)" --list "$$(git branch --show-current)")" ]] || git merge --ff-only

check_no_venv:
	@echo "Checking virtual environment is unset..."
	@[[ -z "$$(poetry env info -p)" ]] || { echo "Poetry virtual environment is already set" && false; }

venv: check_no_venv
	@echo "Creating virtual environment..."
	poetry env use $(PYTHON_VERSION)

check_venv:
	@echo "Checking virtual environment is set..."
	@[[ -n "$$(poetry env info -p)" ]] || { echo "Poetry virtual environment is unset" && false; }
	@[[ "$$("$$(poetry env info -p)/bin/python" -V)" == "Python $(PYTHON_VERSION)" ]] || { echo "Invalid python version of poetry virtual environment" && false; }

install: check_venv
	@echo "Installing python dependencies..."
	poetry install $(SYNC)

clean:
	@echo "Deleting all temporary files..."
	find . -type d -name '__pycache__' -delete || true
	find . -type d -name '.ipynb_checkpoints' -delete || true
	find . -name '.pytest_cache' -delete || true  # ok?
	find . -type f -name '.DS_Store' -delete || true

status: check_venv
	@echo "Reporting file status..."
	du -sh .
	git status

first: pull venv install clean status

recent:	pull install clean status

test: check_venv
	@echo "Running tests..."
	poetry run pytest

push:
	@echo "Pushing file changes..."
	git push

update: check_venv
	@echo "Updating python dependencies..."
	poetry update

shell: check_venv
	@echo "Activating virtual environment in a subshell..."
	poetry shell

runl: check_venv
	@echo "Running locally..."
	poetry run python -m $(PACKAGE_NAME) $(ARGS)

build:
	@echo "Building docker image..."
	docker build --build-arg PYTHON_VERSION=$(PYTHON_VERSION) --build-arg PACKAGE_NAME=$(PACKAGE_NAME) -t $(PROJECT_NAME):$(PROJECT_VERSION) --target=runtime .

rund:
	@echo "Running docker image..."
	docker run -it --env-file .env -v $$(realpath ./logs):/mnt/logs $(PROJECT_NAME):$(PROJECT_VERSION) $(ARGS)

brun: build rund

rbrun: recent build rund
