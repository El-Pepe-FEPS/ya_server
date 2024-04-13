from rest_framework import serializers
from .models import Message, Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'post')


class MessageSerializer(serializers.ModelSerializer):
    chat = ChatSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('user', 'content', 'chat')

    # def create(self, validated_data):
    #     print(validated_data)
    #     chat_data = validated_data.pop['chat']
    #     chat_instance = Chat.objects.get(id=chat_data.get('id'))
    #     return Message.objects.create(chat=chat_instance, **validated_data)
