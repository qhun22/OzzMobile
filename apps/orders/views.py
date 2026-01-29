"""
Orders Views - Đơn hàng
"""
from django.shortcuts import render


def order_list(request):
    """Danh sách đơn hàng"""
    return render(request, 'orders/list.html')


def order_detail(request, order_id):
    """Chi tiết đơn hàng"""
    return render(request, 'orders/detail.html', {'order_id': order_id})

