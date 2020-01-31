FROM python:3.7
LABEL maintainer {{cookiecutter.project_author}} <{{cookiecutter.author_email}}>
RUN apt-get update && \
    apt-get install --yes build-essential postgresql-client \
    libpq-dev curl
RUN mkdir /{{cookiecutter.docker-project-dir}}
WORKDIR /{{cookiecutter.docker-project-dir}}
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
COPY pyproject.toml poetry.lock /{{cookiecutter.docker-project-dir}}/
RUN . $HOME/.poetry/env && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev
COPY . /{{cookiecutter.docker-project-dir}}
CMD [ "sh", "start.sh" ]