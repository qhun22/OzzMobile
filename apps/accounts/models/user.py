"""
User Model - Mô hình người dùng tùy chỉnh
Mở rộng AbstractBaseUser để sử dụng email làm đăng nhập thay vì username
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    Manager tùy chỉnh cho User model
    Xử lý việc tạo user và superuser
    """
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Tạo user thông thường với email và password
        """
        if not email:
            raise ValueError('Email là bắt buộc')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Tạo superuser với quyền admin
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser phải có is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser phải có is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Mô hình người dùng tùy chỉnh cho QHUN22 Mobile
    
    Sử dụng email làm USERNAME_FIELD thay vì username mặc định
    """
    
    # Email - làm username và là duy nhất
    email = models.EmailField(
        'Email',
        unique=True,
        help_text='Email dùng để đăng nhập, không thay đổi được'
    )
    
    # Họ và tên
    first_name = models.CharField(
        'Họ',
        max_length=150,
        blank=True,
        help_text='Họ của người dùng'
    )
    
    last_name = models.CharField(
        'Tên',
        max_length=150,
        blank=True,
        help_text='Tên của người dùng'
    )
    
    # Số điện thoại
    phone_number = models.CharField(
        'Số điện thoại',
        max_length=20,
        blank=True,
        help_text='Số điện thoại liên hệ'
    )
    
    # Ảnh đại diện (tùy chọn)
    avatar = models.ImageField(
        'Ảnh đại diện',
        upload_to='avatars/%Y/%m/',
        blank=True,
        null=True,
        help_text='Ảnh đại diện người dùng (tùy chọn)'
    )
    
    # Trạng thái
    is_active = models.BooleanField(
        'Hoạt động',
        default=True,
        help_text='Cho phép người dùng đăng nhập'
    )
    
    is_staff = models.BooleanField(
        'Nhân viên',
        default=False,
        help_text='Cho phép người dùng truy cập trang admin'
    )
    
    # Thời gian
    date_joined = models.DateTimeField(
        'Ngày tham gia',
        default=timezone.now
    )
    
    # Objects
    objects = UserManager()
    
    # Sử dụng email làm USERNAME_FIELD
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'Người dùng'
        verbose_name_plural = 'Người dùng'
        ordering = ['-date_joined']
    
    def __str__(self):
        """Hiển thị email hoặc tên người dùng"""
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'.strip()
        return self.email
    
    def get_full_name(self):
        """Trả về họ và tên đầy đủ"""
        return f'{self.first_name} {self.last_name}'.strip()
    
    def get_short_name(self):
        """Trả về tên ngắn gọn"""
        return self.first_name or self.email.split('@')[0]
