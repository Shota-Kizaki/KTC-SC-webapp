from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.urls import include
from django.shortcuts import render
urlpatterns = [
    path('login/',LoginView.as_view(redirect_authenticated_user=True,template_name='login/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name="logout"),   # 追加
    path('chat/', include('chat_app.urls'),name="chat"),    # 追加
]

def top(request):
    # ポータルサイトのトップぺージを表示する
    
    # top.htmlをレンダリング
    return render(request, 'login/top.html')

