"""
Apps Cart - Quản lý giỏ hàng
Chức năng: thêm/xóa/sửa sản phẩm trong giỏ hàng
"""
from django.apps import AppConfig


class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cart'
    verbose_name = 'Giỏ hàng'

