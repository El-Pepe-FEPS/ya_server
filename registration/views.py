from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"message": "Email and password are required."}, status=400)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"message": "Invalid email or password."}, status=400)

        if not user.check_password(password):
            return Response({"message": "Invalid email or password."}, status=400)

        login(request, user)

        serialized_user = UserSerializer(user)

        return Response(serialized_user.data)


class RegisterView(APIView):
    def post(self, request):

        serializer = UserSerializer(
            data={
                "name": request.data["name"],
                "surname": request.data["surname"],
                "username": request.data["email"],
                "patronymic": request.data["patronymic"],
                "email": request.data["email"],
                "phone_number": request.data["phone_number"],
                "password": request.data["password"],
            }
        )
        print(serializer)

        serializer.is_valid(raise_exception=True)

        if CustomUser.objects.filter(email=request.data["email"][0]).exists():
            return Response({"message": "Email is already in use."})

        serializer.save()

        return Response(serializer.data)


class CSRFView(APIView):
    def get(self, request):
        return Response({"token": get_token(request)})
