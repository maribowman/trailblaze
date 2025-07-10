FROM python:3.13-slim-bookworm

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv
RUN uv sync
COPY . .

VOLUME /app/data
EXPOSE 8080

ENTRYPOINT ["python", "main.py"]
