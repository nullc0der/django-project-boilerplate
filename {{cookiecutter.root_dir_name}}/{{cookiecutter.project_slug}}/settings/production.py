{%- if cookiecutter.add_sentry == 'Yes' -%}
import sentry_sdk
{% endif -%}
from .base import *

DEBUG = False

ALLOWED_HOSTS = get_env_var("ALLOWED_HOSTS").split(",")

DATABASES = {
    "default": {
        {%- if cookiecutter.database_backend == "postgresql" -%}
        "ENGINE": "django.db.backends.postgresql",
        {%- elif cookiecutter.database_backend == "mysql" -%}
        'ENGINE': 'django.db.backends.mysql',
        {% endif %}
        'NAME': get_env_var('DJANGO_DATABASE_NAME'),
        'USER': get_env_var('DJANGO_DATABASE_USERNAME'),
        'PASSWORD': get_env_var('DJANGO_DATABASE_PASSWORD'),
        'HOST': get_env_var('DJANGO_DATABASE_HOST'),
        'PORT': '',
    }
}

STATIC_URL = "/static/"

SECURE_BROWSER_XSS_FILTER = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

{% if cookiecutter.add_sentry == 'Yes' -%}
sentry_sdk.init(
    dsn=get_env_var("SENTRY_DSN"),
    environment=get_env_var("SITE_ENV"),
    send_default_pii=True,
    enable_tracing=True,
    traces_sample_rate=0.3,
    profiles_sample_rate=0.3,
)
{%- endif %}
