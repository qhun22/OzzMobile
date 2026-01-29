"""
Cart Views - Trang giỏ hàng
"""
from django.shortcuts import render


def cart_detail(request):
    """
    Trang chi tiết giỏ hàng
    """
    return render(request, 'cart/cart.html')

