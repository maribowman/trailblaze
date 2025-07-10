FROM python:3.13-slim-bookworm
ARG USER_ID=1000
ARG GROUP_ID=1000

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv
RUN uv sync --system
COPY . .

VOLUME /app/data
EXPOSE 8080

RUN addgroup -g $GROUP_ID appuser && \
  adduser -u $USER_ID -G appuser -s /bin/sh -D appuser
RUN chown -R appuser:appuser /app

ENTRYPOINT ["python", "main.py"]
