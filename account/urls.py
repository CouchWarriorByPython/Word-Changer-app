from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('profile/', index, name='profile'),
    path('register/', reg, name='register')
]