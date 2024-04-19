#!/bin/sh
echo "Starting celery"
celery -A {{cookiecutter.project_slug}} worker -l info 
