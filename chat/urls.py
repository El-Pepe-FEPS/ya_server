from django.urls import path
from . import views

urlpatterns = [
    path('post/chat/<int:post_id>/', views.ChatView.as_view(), name='chat'),
]
