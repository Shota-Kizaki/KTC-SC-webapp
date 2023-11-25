from django.contrib.auth.views import LoginView
from django.urls import path
urlpatterns = [
    path('login/',
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='login/login.html'
        ),
        name='login'),
]
from django.shortcuts import render

def top(request):
    # ポータルサイトのトップぺージを表示する
    
    # top.htmlをレンダリング
    return render(request, 'login/top.html')