{% if cookiecutter.add_celery == "Yes" %}
from .celery import app as celery_app

__all__ = ('celery_app',)
{% endif %}
