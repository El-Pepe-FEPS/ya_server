from django.urls import path

from registration import views

urlpatterns = [
    path("csrf/", views.CSRFView.as_view(), name="csrf"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("logout/", views.LogoutView.as_view(), name="logout")
]
