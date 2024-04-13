from django.urls import path
import views

urlpatterns = [
    path("csrf/", views.CSRFView.as_view(), name="csrf"),
    path("document/", views.DocumentView.as_view(), name="document"),
]
