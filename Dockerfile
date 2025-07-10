FROM zauberzeug/nicegui:latest

RUN apt-get update

WORKDIR /app
COPY pyproject.toml uv.lock /app
RUN pip install uv
RUN uv sync --frozen
COPY . .

VOLUME /app/data
EXPOSE 8080

ENTRYPOINT ["python", "main.py"]
