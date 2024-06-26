"""{{cookiecutter.project_name}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
{% if cookiecutter.add_drf == "Yes" %}
from django.urls import path, include
{% elif cookiecutter.add_drf == "No" %}
from django.urls import path
{% endif %}
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_title = "{{cookiecutter.project_name}} Administration"
admin.site.site_header = "{{cookiecutter.project_name}} Administration"
admin.site.index_title = "{{cookiecutter.project_name}} Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    {% if cookiecutter.add_drf == "Yes" -%}
    path('api/v1/', include('{{cookiecutter.project_slug}}.api_urls')),
    {%- endif %}
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
