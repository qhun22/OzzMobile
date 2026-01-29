# Export views từ product.py để urls.py có thể truy cập
from apps.products.views.product import product_list, product_detail

__all__ = ['product_list', 'product_detail']
