from django.views.decorators.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response
from storages.backends.gcloud import GoogleCloudStorage

from .serializers import DocumentSerializer
from .models import Document


class DocumentView(APIView):
    def post(self, request):
        serializer = DocumentSerializer(
            data={
                "doc_image": request.data["doc_image"],
                "doc_title": request.data["doc_title"],
                "user": request.user.id
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        gcs = GoogleCloudStorage()
        file_path = serializer.data['doc_image']
        gcs.save(file_path, request.data["doc_image"])

        return Response(serializer.data)


class CSRFView(APIView):
    def get(self, request):
        return Response({"token": get_token(request)})
