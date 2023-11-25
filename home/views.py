from django.shortcuts import render

# Create your views here.
def index(request):
    # ポータルサイトのトップぺージを表示する
    
    # top.htmlをレンダリング
    return render(request, 'home/index.html')