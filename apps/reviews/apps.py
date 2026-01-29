"""
Apps Reviews - Đánh giá sản phẩm
Chức năng: gửi đánh giá, duyệt đánh giá, hiển thị đánh giá
"""
from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.reviews'
    verbose_name = 'Đánh giá'

