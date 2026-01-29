"""
Home URLs - Cấu hình URL trang chủ
Các URL:
- / (trang chủ)
- /about/ (giới thiệu)
- /contact/ (liên hệ)
"""
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
]
