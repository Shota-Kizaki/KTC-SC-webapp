# my_app/admin.py

from django.contrib import admin
from .models import ChatLog

admin.site.register(ChatLog)
