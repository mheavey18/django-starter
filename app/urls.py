from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from app.views import (
    UserListView,
    signup,
)

urlpatterns = [
    path('users/', UserListView.as_view(template_name='app/users.html'), name='users'),
]
