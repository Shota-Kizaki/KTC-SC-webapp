import logging
import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    # ポータルサイトのトップぺージを表示する
    
    # top.htmlをレンダリング
    return render(request, 'home/index.html')
