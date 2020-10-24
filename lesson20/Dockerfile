FROM python:3.7.9-buster

WORKDIR /app

# install and configure poetry for requirements version control
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY money/pyproject.toml money/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY money .

CMD ["python", "main.py"]