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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ClassDataForm
from django.contrib import messages

urlpatterns = [
    path('login/',LoginView.as_view(redirect_authenticated_user=True,template_name='login/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name="logout"),   # 追加
    path('chat/', include('chat_app.urls'),name="chat"),    # 追加
    path('logs/', include('chat_app.urls'),name='chat_logs'),    # 追加
    path('database/', LogoutView.as_view(template_name='login/database.html'), name="database"),   # 追加
]

def top(request):
    # ポータルサイトのトップぺージを表示する
    
    # top.htmlをレンダリング
    return render(request, 'login/top.html')


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "login/signup.html"
    success_url = reverse_lazy("login")
    

    def form_valid(self, form):
        user = form.save()
        group = form.cleaned_data.get('group')
        if group:
            group.user_set.add(user)  # 選択されたグループにユーザーを追加
        # login(self.request, user)  # この行をコメントアウトまたは削除
        return HttpResponseRedirect(self.get_success_url())
    
@login_required


def add_classdata(request):
    if request.method == 'POST':
        form = ClassDataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '登録に成功しました！')  # 成功メッセージを追加
    else:
        form = ClassDataForm()

    return render(request, "login/database.html", {'form': form})