"""
QHUN22 Mobile - Root URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('apps.home.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('products/', include('apps.products.urls')),
    path('cart/', include('apps.cart.urls')),
    path('orders/', include('apps.orders.urls')),
    path('reviews/', include('apps.reviews.urls')),
    path('promotions/', include('apps.promotions.urls')),
    path('payments/', include('apps.payments.urls')),
    path('admin/', include('apps.admin_dashboard.urls')),
]

# Serve media files trong development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

