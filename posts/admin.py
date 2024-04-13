from django.contrib import admin

from .models import HelpRequest, Category

admin.site.register(HelpRequest)
admin.site.register(Category)