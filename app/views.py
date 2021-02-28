from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import User  # change this to custom user
from django.views.generic.list import ListView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from app.forms import SignUpForm


class UserListView(LoginRequiredMixin, ListView):
    model = User


def signup(request):
    if request.method == 'POST':
        # this can't be used with custom user model
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(
                username=username,
                password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
