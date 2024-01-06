ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}-bookworm as builder

ARG PACKAGE_NAME

ARG POETRY_VERSION

RUN pip install poetry==${POETRY_VERSION}

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN mkdir ${PACKAGE_NAME}

RUN touch ${PACKAGE_NAME}/__init__.py

RUN touch README.md

RUN poetry install --sync --without dev && rm -rf $POETRY_CACHE_DIR

FROM python:${PYTHON_VERSION}-slim-bookworm as runtime

ARG PACKAGE_NAME

ARG PROJECT_NAME

WORKDIR /app

COPY --from=builder /app/.venv .venv

COPY ${PACKAGE_NAME} ${PACKAGE_NAME}

COPY pyproject.toml ./

RUN touch .dev

RUN ln -s .venv/bin/${PROJECT_NAME} run

ENTRYPOINT [ "./run" ]
