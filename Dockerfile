FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:0.9.11 /uv /uvx /bin/

# Slim doesn't have git, install it manually
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

ENV UV_NO_DEV=1 \
    UV_PYTHON_DOWNLOADS=0

WORKDIR /app

COPY ./pyproject.toml ./uv.lock /app/

RUN uv sync --locked

COPY ./latest_changes /app/latest_changes

ENV PYTHONPATH=/app \
    PATH="/app/.venv/bin:$PATH"

# Put the image's baked-in venv first on PATH. `uv run` would execute in the
# mounted consumer repo and pick up its `.python-version`, provisioning a Python
# we don't ship.
CMD ["python", "-m", "latest_changes"]
