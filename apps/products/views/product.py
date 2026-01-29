"""
Products Views - Trang sản phẩm
"""
from django.shortcuts import render, get_object_or_404
from apps.products.models import Product


def product_list(request):
    """
    Trang danh sách sản phẩm
    """
    products = Product.objects.filter(is_active=True)
    return render(request, 'products/product/list.html', {
        'products': products,
    })


def product_detail(request, slug):
    """
    Trang chi tiết sản phẩm
    """
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'products/product/detail.html', {
        'product': product,
    })

