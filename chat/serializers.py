from rest_framework import serializers

from registration.models import CustomUser
from posts.models import Post
from .models import Message, Chat


class UserForChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "name", "surname", "patronymic", "phone_number")


class ChatSerializer(serializers.ModelSerializer):
    sender = UserForChatsSerializer(read_only=True)
    recipient = UserForChatsSerializer(read_only=True)

    class Meta:
        model = Chat
        fields = ('id', 'post', 'sender', 'recipient')

    def create(self, validated_data):
        sender = self.context['request'].user
        post = validated_data.get('post')
        post = Post.objects.filter(id=post.id).first()
        recipient = post.user
        return Chat.objects.create(sender=sender, recipient=recipient, **validated_data)


class MessageSerializer(serializers.ModelSerializer):
    chat = ChatSerializer()
    user = UserForChatsSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('user', 'content', 'chat')

    def create(self, validated_data):
        chat_data = validated_data.pop('chat')
        chat_instance, _ = Chat.objects.get_or_create(**chat_data)
        user = self.context['request'].user
        message = Message.objects.create(chat=chat_instance, user=user, **validated_data)
        return message
