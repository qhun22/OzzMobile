"""
Products URLs - Cấu hình URL sản phẩm
"""
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'),
    path('search/', views.product_list, name='search'),
    path('<slug:slug>/', views.product_detail, name='detail'),
]
