from django.db import models
from registration.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class HelpRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
