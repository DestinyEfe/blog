from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    post = User.objects.all()
    return render(request, 'users/home.html', {'post':post})


def about(request):
    return render(request, 'users/about.html')




