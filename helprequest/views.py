from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import HelpRequestSerializer, CategorySerializer
from .models import Category, HelpRequest


class HelpRequestView(APIView):

    def post(self, request):
        serializer = HelpRequestSerializer(data={
            'user': request.user.id,
            'title': request.data['title'],
            'description': request.data['description'],
            'category': request.data['category'],
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def get(self, request):
        queryset = HelpRequest.objects.all()
        serializer = HelpRequestSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
