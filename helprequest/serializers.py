from rest_framework import serializers
from .models import HelpRequest, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class HelpRequestSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = HelpRequest
        fields = ("title", "description", "category")

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_instance = Category.objects.get(title=category_data.get("title"))
        return HelpRequest.objects.create(category=category_instance, **validated_data)
