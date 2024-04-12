from django.urls import path

from registration import views

urlpatterns = [
    path("csrf/", views.get_csrf, name="csrf"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
]
