"""
Apps Promotions - Quản lý khuyến mãi và coupon
Chức năng: chương trình giảm giá, mã voucher
"""
from django.apps import AppConfig


class PromotionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.promotions'
    verbose_name = 'Khuyến mãi'

