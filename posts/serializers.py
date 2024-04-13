from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ("user", "title", "description", "category", "type")

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_instance = Category.objects.get(title=category_data.get("title"))
        return Post.objects.create(category=category_instance, **validated_data)
