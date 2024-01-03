ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}-bookworm as builder

RUN pip install poetry==1.7.0

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --sync --without dev --no-root && rm -rf $POETRY_CACHE_DIR

FROM python:${PYTHON_VERSION}-slim-bookworm as runtime

ARG PACKAGE_NAME

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    PACKAGE_NAME=${PACKAGE_NAME}

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY ${PACKAGE_NAME}/*.py ./${PACKAGE_NAME}/
COPY pyproject.toml ./

ENTRYPOINT python -m ${PACKAGE_NAME} "$0" "$@"
