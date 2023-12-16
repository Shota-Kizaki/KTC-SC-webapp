from django.urls import path
from . import views
urlpatterns = [
    path('chat_app/', views.chat, name='chat'),
    path('logs/', views.log_list, name='log_list'),
    path('download-logs/', views.download_logs, name='download_logs'),
]
