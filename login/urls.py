from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='login/login.html'
    ), name='login'),
]