# Export views từ order.py để urls.py có thể truy cập
from apps.orders.views.order import order_list, order_detail

__all__ = ['order_list', 'order_detail']
