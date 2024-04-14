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
        chat = Chat.objects.filter(post=post_id).first()
        if not chat:
            if post.user_id != request.user.id:
                serializer = ChatSerializer(data={
                    'sender': request.user.id,
                    'recipient': post.user_id,
                    'post': post.id
                }, context={'request': request})
            else:
                return Response({"message": "You cannot create a chat for your own post"}, status=status.HTTP_400_BAD_REQUEST)

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        elif chat:
            serializer = MessageSerializer(data={
                'user': request.user.id,
                'content': request.data['content'],
                'chat': {'id': chat.id, 'post': post_id}
            })

            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    def get(self, request, post_id):
        queryset1 = Chat.objects.filter(post=post_id).first()
        queryset2 = Message.objects.filter(chat=queryset1.id).all()
        serializer = MessageSerializer(queryset2, many=True)
        return Response(serializer.data)


class AllChatView(APIView):
    def get(self, request):
        queryset = Chat.objects.filter(Q(sender=request.user) | Q(recipient=request.user)).all()


        queryset = queryset.distinct()

        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)
























        # try:
        #     post = Post.objects.get(pk=post_id)
        # except Post.DoesNotExist:
        #     return Response({"message": "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)
        #
        # chat = Chat.objects.create(post=post)
        #
        # message_data = {
        #     'user': request.user.id,
        #     'content': request.data.get('content'),
        #     'chat': chat.id
        # }
        # message_serializer = MessageSerializer(data=message_data)
        # if message_serializer.is_valid():
        #     message_serializer.save()
        #     chat_serializer = ChatSerializer(chat)
        #     return Response({"message": "Message sent", "chat": chat_serializer.data}, status=status.HTTP_201_CREATED)
        # return Response(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
