"""quickstartproject URLの設定

`urlpatterns`リストはURLをビューにルーティングします。詳細については以下を参照してください：
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
例：
関数ベースのビュー
    1. インポートを追加：from my_app import views
    2. URLをurlpatternsに追加：path('', views.home, name='home')
クラスベースのビュー
    1. インポートを追加：from other_app.views import Home
    2. URLをurlpatternsに追加：path('', Home.as_view(), name='home')
別のURLconfを含める
    1. include()関数をインポート：from django.urls import include, path
    2. URLをurlpatternsに追加：path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('top.urls')),
    path('', include('chat_app.urls')),    # appアプリケーションのurls.pyを読み込むように追加
    path('admin/', admin.site.urls),
]
