from django.shortcuts import render

# Create your views here.


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            error_message = "Invalid username or password."
            return None

        return HttpResponse(request, {"username": username, "password": password})


def logout_view(request):
    logout(request)


def registration(request):
    pass
