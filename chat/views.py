from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Chat, Message
from posts.models import Post
from .serializers import MessageSerializer, ChatSerializer


class ChatView(APIView):
    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)
        chat = Chat.objects.filter(post=post_id).first()
        if not chat:
            serializer = ChatSerializer(data={
                'post': post.id
            })

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
