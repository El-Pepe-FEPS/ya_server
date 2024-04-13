from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:post_id>/chat/', views.ChatView.as_view(), name='chat'),
]
