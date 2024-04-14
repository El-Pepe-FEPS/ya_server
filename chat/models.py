from django.db import models

from posts.models import Post
from registration.models import CustomUser


# Create your models here.
class Chat(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name='user_sender')
    recipient = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name='user_recipient')

    def __str__(self):
        return self.post.title


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message №{self.id} by {self.user.username}"
