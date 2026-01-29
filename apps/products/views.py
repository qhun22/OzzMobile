"""
Products Views - Sản phẩm và danh mục
"""
from django.shortcuts import render


def product_list(request):
    """Danh sách sản phẩm"""
    return render(request, 'products/list.html')


def product_detail(request, slug):
    """Chi tiết sản phẩm"""
    return render(request, 'products/detail.html', {'slug': slug})


def category_detail(request, slug):
    """Danh mục sản phẩm"""
    return render(request, 'products/category.html', {'slug': slug})

