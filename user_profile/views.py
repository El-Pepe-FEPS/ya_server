from django.core import serializers
from django.views.decorators.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response
from registration.models import CustomUser
from rest_framework.generics import ListAPIView
from rest_framework import status
from registration.serializers import UserSerializer


class ProfileView(APIView):
    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)