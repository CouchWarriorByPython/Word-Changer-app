from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    # path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('profile/<uuid:user_id>/', UserProfileView.as_view(), name='profile'),
    path('register/', RegisterUser.as_view(), name='register')
]