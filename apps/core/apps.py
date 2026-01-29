"""
Apps Core - Ứng dụng cốt lõi của hệ thống
Chứa các thành phần dùng chung: utils, mixins, signals, context processors
"""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Core'

