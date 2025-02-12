from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("registration.urls")),
    path('', include("document.urls")),
    path('', include("user_profile.urls")),
    path('', include("chat.urls")),
    path('accounts/', include("allauth.urls")),
    path('', include("posts.urls")),
]
