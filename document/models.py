from django.db import models
from registration.models import CustomUser


class Document(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doc_image = models.CharField(max_length=200)
    doc_title = models.CharField(max_length=150)
