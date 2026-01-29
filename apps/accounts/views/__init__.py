# Export views từ auth.py để urls.py có thể truy cập
from apps.accounts.views.auth import login_view, register_view, forgot_password_view, profile_view, logout_view

__all__ = ['login_view', 'register_view', 'forgot_password_view', 'profile_view', 'logout_view']
