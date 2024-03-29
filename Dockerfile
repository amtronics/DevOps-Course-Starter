FROM python:3.9-buster as base
RUN pip3 install poetry
WORKDIR /opt/app
COPY . /opt/app
RUN poetry config virtualenvs.create false && poetry install

FROM base as production
ENV WEBAPP_PORT=8000
EXPOSE ${WEBAPP_PORT}
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind=0.0.0.0", "todo_app.app:create_app()"]

FROM base as development
ENV WEBAPP_PORT=5000
EXPOSE ${WEBAPP_PORT}
ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

# testing stage
FROM base as test
ENTRYPOINT ["poetry", "run", "pytest"]