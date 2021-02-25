from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def detail(request, user_name):
    return HttpResponse("Logged in as user %s." % user_name)
