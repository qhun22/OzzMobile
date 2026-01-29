"""
Admin Dashboard Views - Trang quản trị
"""
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import redirect

from apps.accounts.models import User


def is_admin(user):
    """Kiểm tra user có phải admin không"""
    return user.is_authenticated and (user.is_staff or user.is_superuser)


@user_passes_test(is_admin, login_url='/accounts/login/')
def dashboard_view(request):
    """
    Trang quản trị - Bảng điều khiển
    """
    # Thống kê
    total_members = User.objects.count()
    
    from django.utils import timezone
    from datetime import datetime, timedelta
    
    # Thành viên mới hôm nay
    today = timezone.now().date()
    new_members_today = User.objects.filter(date_joined__date=today).count()
    
    # Tổng số sản phẩm (nếu model tồn tại)
    try:
        from apps.products.models import Product
        total_products = Product.objects.count()
    except ImportError:
        total_products = 0
    
    # Tổng số đơn hàng (nếu model tồn tại)
    try:
        from apps.orders.models import Order
        total_orders = Order.objects.count()
    except ImportError:
        total_orders = 0
    
    context = {
        'total_members': total_members,
        'new_members_today': new_members_today,
        'total_products': total_products,
        'total_orders': total_orders,
    }
    
    return render(request, 'admin_dashboard/dashboard.html', context)

