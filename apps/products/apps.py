"""
Apps Products - Quản lý sản phẩm và danh mục
Chức năng: danh mục, sản phẩm, hình ảnh, thông số kỹ thuật
"""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'
    verbose_name = 'Sản phẩm'

