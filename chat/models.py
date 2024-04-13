from django.db import models

from posts.models import Post
from registration.models import CustomUser


# Create your models here.
class Chat(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Chat {self.id}"


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message {self.id} by {self.user.username}"
