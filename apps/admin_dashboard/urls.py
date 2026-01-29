"""
Admin Dashboard URLs - Cấu hình URL trang quản trị
"""
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='admin_dashboard'),
]
