#!/bin/sh
git init
git add .
git commit -m "initial commit"
echo "Following commands assumes you have poetry installed"
poetry install
{% if cookiecutter.add_sentry == "Yes" %}
poetry add sentry-sdk
{% endif %}
{% if cookiecutter.add_drf == "Yes" %}
poetry add djangorestframework
{% endif %}
