from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import top
from home.views import home  # homeアプリからhomeビューをインポート

from . import views  # Add this import statement

urlpatterns = [
    path('login/',
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='login/login.html'
        ),
        name='login'),
    path('', top, name='top'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('sieving/', views.SievingView, name="sieving"),  # 末尾にスラッシュを追加
    path('home/', home, name="home"),  # homeビューへのリンクを追加
]
