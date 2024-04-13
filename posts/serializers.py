from rest_framework import serializers

from registration.models import CustomUser
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class UserForPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("name", "surname", "patronymic", "email", "phone_number", "bio")


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = UserForPostsSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ("user", "title", "description", "category", "type", "id")

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_instance = Category.objects.get(title=category_data.get("title"))
        user = self.context['request'].user
        return Post.objects.create(category=category_instance, user=user, **validated_data)
