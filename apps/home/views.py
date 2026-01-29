"""
Home Views - Trang chủ
Chức năng: hiển thị trang chủ website
"""
from django.shortcuts import render


def index(request):
    """
    Trang chủ QHUN22 Mobile
    Hiển thị sản phẩm nổi bật và danh mục
    """
    context = {
        'page_title': 'Trang chủ',
    }
    return render(request, 'home/index.html', context)

