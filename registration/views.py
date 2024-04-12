from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import get_token
from django.http import JsonResponse
from .models import CustomUser
from .utils import generate_username


def get_csrf(request):
    return JsonResponse({"token": get_token(request)})


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        username = CustomUser.objects.get(email=email).username
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            return JsonResponse({"message": "Invalid username or password."})

        return JsonResponse(user.toJSON())


def logout_view(request):
    logout(request)


def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        username = generate_username()

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({"message": "Email is already in use."})

        user = CustomUser.objects.create_user(
            username=username, email=email, password=password
        )

        return JsonResponse(user.toJSON())
