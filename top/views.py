from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.urls import include
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import Group
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy

from .forms import SignUpForm

urlpatterns = [
    path('login/',LoginView.as_view(redirect_authenticated_user=True,template_name='login/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name="logout"),   # 追加
    path('chat/', include('chat_app.urls'),name="chat"),    # 追加
]

def top(request):
    # ポータルサイトのトップぺージを表示する
    
    # top.htmlをレンダリング
    return render(request, 'login/top.html')


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "login/signup.html"
    success_url = reverse_lazy("top")

    def form_valid(self, form):
        user = form.save()
        group = form.cleaned_data['group']
        group.user_set.add(user)  # 選択されたグループにユーザーを追加
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())
