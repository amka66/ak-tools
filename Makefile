MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

.PHONY: pull check_no_venv venv check_venv install clean status first recent test push update shell runl rerunl build rund brun rebrun repro rerep
# .EXPORT_ALL_VARIABLES:
# .DELETE_ON_ERROR:
# .INTERMEDIATE:
# .SECONDARY:
.DEFAULT_GOAL := status

ARGS ?=
PI ?= dvc.yaml

ENABLE_DVC ?= 0
ENABLE_TEST ?= 0
SYNC_DVC_CACHE ?= 0
SYNC_POETRY_INSTALL ?= 1

ifeq ($(SYNC_DVC_CACHE),1)
RUN_CACHE = --run-cache
else
RUN_CACHE =
endif

ifeq ($(SYNC_POETRY_INSTALL),1)
SYNC = --sync
else
SYNC =
endif

PROJECT_NAME = $(shell poetry version | cut -d' ' -f1)
PACKAGE_NAME = $(shell poetry version | cut -d' ' -f1 | tr '-' '_')
PROJECT_VERSION = $(shell poetry version | cut -d' ' -f2)
PYTHON_VERSION = $(shell cat .python-version)
rightparenthesis := )
POETRY_VERSION = $(shell poetry --version | cut -d' ' -f3 | cut -d'$(rightparenthesis)' -f1)

pull:
	@echo "Pulling file changes..."
	git fetch --all --tags
	[[ -z  "$$(git branch --format "%(upstream:short)" --list "$$(git branch --show-current)")" ]] || git merge --ff-only
ifeq ($(ENABLE_DVC),1)
	poetry run dvc fetch $(RUN_CACHE)
	-poetry run dvc checkout
endif

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
	@echo "Deleting temporary files..."
	find . -type f -name '.DS_Store' -delete || true
	poetry run cleanpy --include-builds .
	find . -type d -name '.ipynb_checkpoints' -delete || true

status: check_venv
	@echo "Reporting file status..."
	du -sh .
	git status
ifeq ($(ENABLE_DVC),1)
	poetry run dvc status
	poetry run dvc data status --granular
	poetry run dvc diff
	poetry run dvc params diff
	poetry run dvc metrics diff
	# poetry run dvc plots diff
	poetry run dvc status --cloud
endif

first: pull venv install clean status

recent:	pull install clean status

ifeq ($(ENABLE_TEST),1)
test: check_venv
	@echo "Running tests..."
	poetry run pytest
endif

push: test
	@echo "Pushing file changes..."
ifeq ($(ENABLE_DVC),1)
	poetry run dvc push $(RUN_CACHE)
endif
	git push

update: check_venv
	@echo "Updating python dependencies..."
	poetry update

shell: check_venv
	@echo "Activating virtual environment in a subshell..."
	poetry shell

runl: check_venv
	@echo "Running locally (args=$(ARGS))..."
	poetry run $(PROJECT_NAME) $(ARGS)

rerunl: recent runl

build:
	@echo "Building docker image..."
	docker build --build-arg PYTHON_VERSION=$(PYTHON_VERSION) \
				 --build-arg PACKAGE_NAME=$(PACKAGE_NAME) \
				 --build-arg PROJECT_NAME=$(PROJECT_NAME) \
				 --build-arg POETRY_VERSION=$(POETRY_VERSION) \
				 -t $(PROJECT_NAME):$(PROJECT_VERSION) --target=runtime .

rund:
	@echo "Running docker image (args=$(ARGS))..."
	docker run -it --env-file .secrets \
				   --env-file .env \
				   -v $$(realpath ./logs):/app/logs \
				   $(PROJECT_NAME):$(PROJECT_VERSION) $(ARGS)

brun: build rund

rebrun: recent build rund

ifeq ($(ENABLE_DVC),1)
repro: check_venv
	@echo "Reproducing pipeline $(PI)..."
	poetry run dvc repro $(PI)

rerep: recent repro status
endif
