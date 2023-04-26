FROM python:3.7-buster
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -
WORKDIR /opt/app
ENV PATH=/opt/poetry/bin:$PATH
ENV WEBAPP_PORT=8000
EXPOSE ${WEBAPP_PORT}
COPY . /opt/app
RUN poetry config virtualenvs.create false && poetry install
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind=0.0.0.0", "todo_app.app:create_app()"]