"""
Product Model - Mô hình sản phẩm
Lưu trữ thông tin điện thoại di động
"""
from decimal import Decimal
from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    """
    Mô hình sản phẩm điện thoại di động
    
    Lưu trữ thông tin cơ bản của sản phẩm:
    - Tên, mô tả, giá, tồn kho
    - Liên kết với danh mục
    """
    
    # Tên sản phẩm
    name = models.CharField(
        'Tên sản phẩm',
        max_length=500,
        help_text='Tên đầy đủ của sản phẩm'
    )
    
    # Slug cho URL thân thiện
    slug = models.SlugField(
        'Slug',
        max_length=500,
        unique=True,
        help_text='Đường dẫn thân thiện (tự động tạo từ tên)'
    )
    
    # Danh mục (sử dụng string reference để tránh circular import)
    category = models.ForeignKey(
        'products.Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        verbose_name='Danh mục',
        help_text='Danh mục sản phẩm'
    )
    
    # Mô tả ngắn
    short_description = models.TextField(
        'Mô tả ngắn',
        max_length=500,
        blank=True,
        help_text='Mô tả ngắn hiển thị trong danh sách sản phẩm'
    )
    
    # Mô tả chi tiết (HTML allowed)
    description = models.TextField(
        'Mô tả chi tiết',
        blank=True,
        help_text='Mô tả đầy đủ sản phẩm (hỗ trợ HTML)'
    )
    
    # Thông số kỹ thuật (JSON)
    specifications = models.JSONField(
        'Thông số kỹ thuật',
        default=dict,
        blank=True,
        help_text='Thông số kỹ thuật dạng JSON (RAM, Pin, Màn hình...)'
    )
    
    # Giá
    price = models.DecimalField(
        'Giá bán',
        max_digits=12,
        decimal_places=0,
        help_text='Giá bán (VND)'
    )
    
    # Giá gốc (để so sánh, optional)
    original_price = models.DecimalField(
        'Giá gốc',
        max_digits=12,
        decimal_places=0,
        default=Decimal('0'),
        help_text='Giá gốc (để hiển thị giảm giá)'
    )
    
    # Số lượng trong kho
    stock = models.PositiveIntegerField(
        'Số lượng tồn kho',
        default=0,
        help_text='Số lượng sản phẩm còn trong kho'
    )
    
    # SKU - Mã sản phẩm
    sku = models.CharField(
        'SKU',
        max_length=100,
        unique=True,
        help_text='Mã sản phẩm (SKU) duy nhất'
    )
    
    # Trạng thái
    is_active = models.BooleanField(
        'Hoạt động',
        default=True,
        help_text='Sản phẩm có hiển thị trên website không'
    )
    
    is_featured = models.BooleanField(
        'Nổi bật',
        default=False,
        help_text='Sản phẩm nổi bật hiển thị trang chủ'
    )
    
    # Thời gian
    created_at = models.DateTimeField(
        'Ngày tạo',
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        'Ngày cập nhật',
        auto_now=True
    )
    
    class Meta:
        verbose_name = 'Sản phẩm'
        verbose_name_plural = 'Sản phẩm'
        ordering = ['-created_at']
    
    def __str__(self):
        """Hiển thị tên sản phẩm"""
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Tự động tạo slug từ tên nếu chưa có
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    @property
    def is_in_stock(self):
        """Kiểm tra còn hàng không"""
        return self.stock > 0
    
    @property
    def discount_percent(self):
        """Tính phần trăm giảm giá"""
        if self.original_price and self.original_price > self.price:
            discount = ((self.original_price - self.price) / self.original_price) * 100
            return round(discount)
        return 0
    
    @property
    def formatted_price(self):
        """Trả về giá đã định dạng"""
        return f'{self.price:,.0f}₫'
