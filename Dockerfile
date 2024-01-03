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

ENV PACKAGE_NAME=${PACKAGE_NAME}

COPY --from=builder /app/.venv /app/.venv

COPY ${PACKAGE_NAME}/*.py ${PACKAGE_NAME}/

COPY pyproject.toml ./

RUN ln -s ${PACKAGE_NAME} src  # this will change the package name to src inside docker # TODO
RUN ln -s /mnt/logs logs

ENTRYPOINT ["/app/.venv/bin/python", "-m", "src"]
