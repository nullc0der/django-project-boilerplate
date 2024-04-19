FROM python:3.10
LABEL maintainer {{cookiecutter.project_author}} <{{cookiecutter.author_email}}>
RUN apt-get update && \
    apt-get install --yes build-essential curl
{% if cookiecutter.database_backend == 'postgresql' -%}
RUN apt-get install --yes postgresql-client libpq-dev
{% elif cookiecutter.database_backend == 'mysql' -%}
RUN apt-get install --yes mysql-client
{% endif -%}
RUN mkdir /{{cookiecutter.docker_project_dir}}
WORKDIR /{{cookiecutter.docker_project_dir}}
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY pyproject.toml poetry.lock /{{cookiecutter.docker_project_dir}}/
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev
COPY . /{{cookiecutter.docker_project_dir}}
CMD [ "sh", "start.sh" ]
