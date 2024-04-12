from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import CustomUser


def login_view(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
        else:
            error_message = "Invalid username or password."
            return None

        return HttpResponse(request, {"email": email, "password": password})


def logout_view(request):
    logout(request)


def register(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        user = CustomUser.objects.create_user(email=email, password=password)

    else:
        return HttpResponse(request)
