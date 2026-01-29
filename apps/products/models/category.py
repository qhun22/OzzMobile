"""
Category Model - Mô hình danh mục sản phẩm
Hỗ trợ cấu trúc parent-child (danh mục cha - danh mục con)
"""
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class CategoryManager(models.Manager):
    """
    Manager tùy chỉnh cho Category
    Cung cấp các phương thức tiện ích
    """
    
    def active(self):
        """Lấy danh mục đang hoạt động"""
        return self.filter(is_active=True)
    
    def roots(self):
        """Lấy danh mục gốc (không có parent)"""
        return self.filter(parent__isnull=True, is_active=True)


class Category(models.Model):
    """
    Mô hình danh mục sản phẩm
    
    Hỗ trợ phân cấp danh mục:
    - Ví dụ: Điện thoại -> Apple -> iPhone 15
    - Hoặc: Điện thoại -> Samsung -> Galaxy S24
    """
    
    # Tên danh mục
    name = models.CharField(
        'Tên danh mục',
        max_length=200,
        help_text='Tên hiển thị của danh mục'
    )
    
    # Slug cho URL thân thiện
    slug = models.SlugField(
        'Slug',
        max_length=200,
        unique=True,
        help_text='Đường dẫn thân thiện (tự động tạo từ tên)'
    )
    
    # Danh mục cha (optional - cho phân cấp)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Danh mục cha',
        help_text='Danh mục cha (để trống nếu là danh mục gốc)'
    )
    
    # Hình ảnh đại diện (tùy chọn)
    image = models.ImageField(
        'Hình ảnh',
        upload_to='categories/%Y/%m/',
        blank=True,
        null=True,
        help_text='Hình ảnh đại diện danh mục (tùy chọn)'
    )
    
    # Mô tả ngắn
    description = models.TextField(
        'Mô tả',
        blank=True,
        help_text='Mô tả ngắn về danh mục'
    )
    
    # Thứ tự hiển thị
    order = models.PositiveIntegerField(
        'Thứ tự',
        default=0,
        help_text='Thứ tự hiển thị (số nhỏ hiển thị trước)'
    )
    
    # Trạng thái
    is_active = models.BooleanField(
        'Hoạt động',
        default=True,
        help_text='Danh mục có hiển thị trên website không'
    )
    
    # Thời gian tạo
    created_at = models.DateTimeField(
        'Ngày tạo',
        auto_now_add=True
    )
    
    # Thời gian cập nhật
    updated_at = models.DateTimeField(
        'Ngày cập nhật',
        auto_now=True
    )
    
    # Custom manager
    objects = CategoryManager()
    
    class Meta:
        verbose_name = 'Danh mục'
        verbose_name_plural = 'Danh mục'
        ordering = ['order', 'name']
    
    def __str__(self):
        """Hiển thị tên danh mục"""
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Tự động tạo slug từ tên nếu chưa có
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    @property
    def is_root(self):
        """Kiểm tra có phải danh mục gốc không"""
        return self.parent is None
    
    @property
    def level(self):
        """
        Trả về level của danh mục
        0 = gốc, 1 = con của gốc, etc.
        """
        level = 0
        current = self
        while current.parent:
            level += 1
            current = current.parent
        return level
