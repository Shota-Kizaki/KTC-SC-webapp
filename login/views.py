from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.urls import include
from django.shortcuts import render,redirect
#from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/',
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='login/login.html'
        ),
        name='login'),
    path('logout/',
         LogoutView.as_view(
            template_name='login/logout.html'
        ), 
        name="logout"),   # 追加
    path('home/', include('home.urls')),    # 追加
]

def top(request):
    # ポータルサイトのトップぺージを表示する
    
    # top.htmlをレンダリング
    return render(request, 'login/top.html')

@login_required
def SievingView(request):
    if request.user.is_authenticated:
        """ログインユーザーに対する処理"""
        return redirect('/home')  # コンパネに遷移
    else:
        """匿名ユーザーに対する処理"""
        return redirect('/login/logout')  # 強制ログアウト
