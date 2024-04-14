from django.db.models import Q, F
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Chat, Message
from posts.models import Post
from .serializers import MessageSerializer, ChatSerializer
from rest_framework.exceptions import PermissionDenied


class ChatView(APIView):
    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)
        if post.user_id != request.user.id:
            chat = Chat.objects.filter(sender=request.user.id, recipient=post.user_id).first()
            if not chat:
                serializer = ChatSerializer(data={
                    'sender': request.user.id,
                    'recipient': post.user_id,
                    'post': post.id
                }, context={'request': request})
            else:
                return Response({"message": "Your chat already exists"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "You cannot create a chat for your own post"},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class MessageView(APIView):
    def post(self, request, post_id, chat_id):
        serializer = MessageSerializer(data={
            'user': request.user.id,
            'content': request.data['content'],
            'chat': {'id': chat_id, 'post': post_id}
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, post_id, chat_id):
        queryset = Message.objects.filter(chat=chat_id).all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)


class AllChatView(APIView):
    def get(self, request):
        queryset = Chat.objects.filter(Q(sender=request.user) | Q(recipient=request.user)).all()

        queryset = queryset.distinct()

        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)
