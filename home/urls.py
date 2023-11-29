from django.urls import path

from . import views
#from login.views import LogoutView
urlpatterns = [
    path("home/", views.home, name="home"),
    #path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
]