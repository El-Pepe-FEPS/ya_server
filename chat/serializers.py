from rest_framework import serializers
from .models import Message, Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'post')


class MessageSerializer(serializers.ModelSerializer):
    chat = ChatSerializer()

    class Meta:
        model = Message
        fields = ('user', 'content', 'chat')

    def create(self, validated_data):
        chat_data = validated_data.pop('chat')
        chat_instance, _ = Chat.objects.get_or_create(**chat_data)
        message = Message.objects.create(chat=chat_instance, **validated_data)
        return message
