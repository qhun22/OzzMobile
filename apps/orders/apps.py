"""
Apps Orders - Quản lý đơn hàng
Chức năng: tạo đơn hàng, theo dõi trạng thái, lịch sử đơn hàng
"""
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orders'
    verbose_name = 'Đơn hàng'

