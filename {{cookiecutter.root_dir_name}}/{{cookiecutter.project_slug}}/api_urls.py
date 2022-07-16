from django.urls import path, include
from {{cookiecutter.project_slug}}.routers import router

urlpatterns = [
    path('', include(router.urls)),
]
