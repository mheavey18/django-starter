from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.list import ListView


class UserListView(LoginRequiredMixin, ListView):

    model = User
