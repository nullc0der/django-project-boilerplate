#!/bin/sh
echo "Starting celery beat"
celery -A {{cookiecutter.project_slug}} beat -l info 
