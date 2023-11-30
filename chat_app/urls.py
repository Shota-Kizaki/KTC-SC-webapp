from django.urls import path
from . import views
urlpatterns = [
    path('chat_app/', views.chat, name='chat'),
]
