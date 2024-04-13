from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .utils import generate_username
from .serializers import UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = CustomUser.objects.get(email=request.data["email"]).username

        user = authenticate(
            request, username=username, password=request.data["password"]
        )

        if user is None:
            return Response({"message": "Invalid username or password."})

        login(request, user)

        serialized_user = UserSerializer(user)

        return Response(serialized_user.data)


class RegisterView(APIView):
    def post(self, request):
        username = generate_username()

        serializer = UserSerializer(
            data={
                "email": request.data["email"],
                "password": request.data["password"],
                "username": username,
            }
        )

        serializer.is_valid(raise_exception=True)

        if CustomUser.objects.filter(email=request.data["email"][0]).exists():
            return Response({"message": "Email is already in use."})

        serializer.save()

        return Response(serializer.data)


class CSRFView(APIView):
    def get(self, request):
        return Response({"token": get_token(request)})
