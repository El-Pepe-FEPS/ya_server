from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("name", "surname", "patronymic", "email", "phone_number", "bio", "role")

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
