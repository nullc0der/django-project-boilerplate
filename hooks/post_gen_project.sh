#!/bin/sh
git init
git add .
git commit -m "initial commit"
echo "Following commands assumes you have poetry installed"
poetry install
{% if cookiecutter.add_sentry == "Yes" %}
poetry add sentry-sdk[django]
{% endif %}
{% if cookiecutter.add_drf == "Yes" %}
poetry add djangorestframework
{% endif %}
{% if cookiecutter.add_drf == "No" %}
rm -rf {{cookiecutter.project_slug}}/api_urls.py
rm -rf {{cookiecutter.project_slug}}/routers.py
{% endif %}
{% if cookiecutter.add_celery == "Yes" %}
poetry add celery[redis]
{% endif %}
{% if cookiecutter.add_celery == "No" %}
rm -rf {{cookiecutter.project_slug}}/celery.py
rm -rf start_celery.sh
rm -rf start_celery_beat.sh
{% endif %}
