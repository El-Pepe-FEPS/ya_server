from django.urls import path
from . import views

urlpatterns = [
    path('post/chat/<int:post_id>/', views.ChatView.as_view(), name='chat'),
    path('chats/', views.AllChatView.as_view(), name='all_chats'),
]
