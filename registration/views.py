from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import get_token
from rest_framework import status
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
        required_fields = ['name', 'surname', 'patronymic', 'email', 'phone_number', 'password']
        d = {"message":[]}
        for field in required_fields:
            if field not in request.data:
                d["message"].append(f"The field '{field.capitalize()}' is required.")
                return Response(d, status=status.HTTP_400_BAD_REQUEST)
            if request.data[field] == "":
                d["message"].append(f"The field '{field.capitalize()}' is required.")
                return Response(d, status=status.HTTP_400_BAD_REQUEST)
            if "@" not in request.data["email"]:
                d["message"].append(f"Email address is not written correctly.")
                return Response(d, status=status.HTTP_400_BAD_REQUEST)
            if CustomUser.objects.filter(email=request.data.get('email')).exists():
                d['message'].append("Email is already in use.")
                return Response(d, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CSRFView(APIView):
    def get(self, request):
        return Response({"token": get_token(request)})
