from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("registration.urls")),
    path('', include("document.urls")),
    path('accounts/', include("allauth.urls")),
    path('', include("helprequest.urls")),
]
