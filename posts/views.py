from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .serializers import PostSerializer, CategorySerializer
from .models import Category, Post


class PostView(APIView):

    def post(self, request):
        serializer = PostSerializer(data={
            'title': request.data['title'],
            'description': request.data['description'],
            'category': request.data['category'],
            'type': request.data['type'],
        }, context={'request': request})

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            missing_fields = ", ".join(e.detail.keys())
            return Response({"message": f"Field(s) {missing_fields} must be filled"}, status=400)
        serializer.save()

        return Response(serializer.data)


class RequestGetView(APIView):
    def get(self, request):
        queryset = Post.objects.filter(type='help request').all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class OfferGetView(APIView):
    def get(self, request):
        queryset = Post.objects.filter(type='help offer').all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class PostsGetView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
