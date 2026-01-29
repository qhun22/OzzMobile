"""
Apps Accounts - Quản lý tài khoản người dùng
Chức năng: đăng ký, đăng nhập, quản lý profile, địa chỉ
"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    verbose_name = 'Tài khoản'

