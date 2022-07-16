#!/bin/sh
git init
git add .
git commit -m "initial commit"
echo "Following commands assumes you have poetry installed"
poetry install
{% if cookiecutter.add_sentry == "Yes" %}
poetry add sentry-sdk
{% endif %}
