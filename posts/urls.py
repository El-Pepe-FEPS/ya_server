from django.urls import path

from . import views

urlpatterns = [
    path('help_request/', views.HelpRequestView.as_view(), name="Help Request"),
    path('category/', views.CategoryView.as_view(), name='Category'),
]
