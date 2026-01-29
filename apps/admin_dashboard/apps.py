from django.apps import AppConfig


class AdminDashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.admin_dashboard'
    verbose_name = 'Quản trị'
    
    def ready(self):
        """Tạo tài khoản admin mặc định khi khởi động app"""
        from apps.accounts.models import User
        
        # Thông tin admin mặc định
        admin_email = 'admin@qhun22.com'
        admin_password = 'Quanghuyso1#'
        admin_full_name = 'Quang Huy Truong'
        admin_phone = '0327221005'
        
        # Kiểm tra và tạo admin nếu chưa tồn tại
        if not User.objects.filter(email=admin_email).exists():
            try:
                user = User.objects.create_user(
                    email=admin_email,
                    password=admin_password,
                    first_name='Quang Huy',
                    last_name='Truong',
                    phone_number=admin_phone,
                    is_staff=True,
                    is_superuser=True,
                    is_active=True
                )
                print(f'[OK] Admin account created: {admin_email}')
            except Exception as e:
                print(f'[ERROR] Failed to create admin account: {e}')
        else:
            print(f'[OK] Admin account already exists: {admin_email}')

