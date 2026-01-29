"""
Apps Payments - Quản lý thanh toán
Chức năng: tích hợp cổng thanh toán, ghi nhận giao dịch
"""
from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payments'
    verbose_name = 'Thanh toán'

