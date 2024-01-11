from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import top
from chat_app.views import chat, log_list  # homeアプリからhomeビューをインポート

from . import views  # Add this import statement

urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='login/login.html'),name='login'),
    path('', top, name='top'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('chat_app/', chat, name="chat"),  # homeビューへのリンクを追加
    path('logs/', log_list, name='chat_logs'),
    path('database/', views.add_classdata, name='database'),
]
