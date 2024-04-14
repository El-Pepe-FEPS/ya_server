from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:post_id>/', views.ChatView.as_view(), name='create_chat'),
    path('chat/all/', views.AllChatView.as_view(), name='all_chats'),
    path('message/<int:post_id>/<int:chat_id>/', views.MessageView.as_view(), name='messages'),
]
