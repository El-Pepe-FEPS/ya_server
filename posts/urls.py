from django.urls import path

from . import views

urlpatterns = [
    path('post/create', views.PostView.as_view(), name="Post Form"),
    path('post/requests/', views.RequestGetView.as_view(), name='Help Requests'),
    path('post/offers/', views.OfferGetView.as_view(), name='Help Offers'),
    path('post/all', views.PostsGetView.as_view(), name='All Posts'),
    path('category/', views.CategoryView.as_view(), name='Category'),
]
