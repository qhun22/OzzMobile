"""
Orders Views - Trang đơn hàng
"""
from django.shortcuts import render


def order_list(request):
    """
    Trang danh sách đơn hàng
    """
    return render(request, 'orders/order/list.html')


def order_detail(request, order_id):
    """
    Trang chi tiết đơn hàng
    """
    return render(request, 'orders/order/detail.html', {
        'order_id': order_id,
    })

