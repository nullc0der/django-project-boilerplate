#!/bin/sh
{%- if cookiecutter.database_backend == 'postgresql' -%}
while ! pg_isready -h $DJANGO_DATABASE_HOST -p "5432" > /dev/null 2> /dev/null; do
   echo "Waiting for DB host....."
   sleep 1
done
{%- elif cookiecutter.database_backend == 'mysql' -%}
while ! mysqladmin ping -h $DJANGO_DATABASE_HOST -P "3306" --silent; do
   echo "Waiting for DB host....."
   sleep 1
done
{% endif %}
echo "Starting celery"
celery -A {{cookiecutter.project_slug}} worker -l info 
