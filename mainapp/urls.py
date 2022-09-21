from django.urls import path
from .views import *

urlpatterns = [
    path('', DocumentView.as_view(), name='home'),
    path('success/', success, name='success_page'),
    path('download/', download)
]