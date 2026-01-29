"""
Cart URLs - Cấu hình URL giỏ hàng
"""
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='detail'),
]
