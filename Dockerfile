FROM python:3.11.5

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install

RUN poetry add psycopg2-binary

CMD export PYTHONPATH="${PYTHONPATH}:/app/" && poetry run python api/main.py
