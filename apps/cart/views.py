"""
Cart Views - Giỏ hàng
"""
from django.shortcuts import render


def cart_detail(request):
    """Chi tiết giỏ hàng"""
    return render(request, 'cart/cart.html')

