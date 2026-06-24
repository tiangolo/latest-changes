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

ENV PYTHONPATH=/app

CMD ["uv", "run", "python", "-m", "latest_changes"]
