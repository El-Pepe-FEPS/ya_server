from django.db import models
from registration.models import CustomUser


class Document(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doc_image = models.ImageField()
    doc_title = models.CharField(max_length=150)

    def __str__(self):
        return self.doc_title
