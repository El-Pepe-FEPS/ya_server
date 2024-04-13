from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer


class LoginView(APIView):
    def post(self, request):
        email = CustomUser.objects.get(email=request.data["email"]).email

        user = authenticate(
            request, email=email, password=request.data["password"]
        )

        if user is None:
            return Response({"message": "Invalid username or password."})

        login(request, user)

        serialized_user = UserSerializer(user)

        return Response(serialized_user.data)


class RegisterView(APIView):
    def post(self, request):

        serializer = UserSerializer(
            data={
                "name": request.data["name"],
                "surname": request.data["surname"],
                "patronymic": request.data["patronymic"],
                "email": request.data["email"],
                "phone_number": request.data["phone_number"],
                "password": request.data["password"],
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
