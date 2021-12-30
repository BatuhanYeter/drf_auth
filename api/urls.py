from django.urls import re_path, path, include
from django.views.generic import TemplateView
from .views import schema_view

urlpatterns = [
    re_path(r'^$', schema_view)
]
