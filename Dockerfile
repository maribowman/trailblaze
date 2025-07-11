FROM python:3.13-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.6.10 /uv /uvx /bin/
RUN apt-get update

WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN uv sync --locked
COPY . /app

VOLUME /app/data
EXPOSE 6969

ENTRYPOINT ["uv", "run", "main.py"]
