# Export views từ cart.py để urls.py có thể truy cập
from apps.cart.views.cart import cart_detail

__all__ = ['cart_detail']
