"""
Accounts Views - Xác thực và quản lý tài khoản người dùng
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.accounts.models import User


def login_view(request):
    """
    Trang đăng nhập
    """
    if request.user.is_authenticated:
        return redirect('home:index')
    
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        remember_me = request.POST.get('remember_me')
        
        # Validate
        if not email or not password:
            messages.error(request, 'Vui lòng nhập đầy đủ email và mật khẩu')
            return render(request, 'accounts/login.html')
        
        # Authenticate
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Login
            if remember_me:
                request.session.set_expiry(604800)  # 7 days
            else:
                request.session.set_expiry(0)  # Browser close
            
            login(request, user)
            messages.success(request, 'Đăng nhập thành công')
            return redirect('home:index')
        else:
            messages.error(request, 'Email hoặc mật khẩu không đúng')
    
    return render(request, 'accounts/login.html')


def register_view(request):
    """
    Trang đăng ký
    """
    if request.user.is_authenticated:
        return redirect('home:index')
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        
        # Tách họ và tên
        name_parts = full_name.split(' ', 1)
        first_name = name_parts[0] if name_parts else ''
        last_name = name_parts[1] if len(name_parts) > 1 else ''
        
        # Validate required fields
        errors = []
        
        if not full_name:
            errors.append('Họ và tên là bắt buộc')
        if not email:
            errors.append('Email là bắt buộc')
        if not phone_number:
            errors.append('Số điện thoại là bắt buộc')
        if not password:
            errors.append('Mật khẩu là bắt buộc')
        if password != confirm_password:
            errors.append('Mật khẩu không khớp')
        if len(password) < 6:
            errors.append('Mật khẩu phải có ít nhất 6 ký tự')
        
        # Check unique email
        if email and User.objects.filter(email=email).exists():
            errors.append('Email đã tồn tại')
        
        # Check unique phone
        if phone_number and User.objects.filter(phone_number=phone_number).exists():
            errors.append('Số điện thoại đã tồn tại')
        
        if errors:
            # Hiển thị lỗi đầu tiên qua toast
            messages.error(request, errors[0])
        else:
            # Create user
            user = User.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number
            )
            
            # Auto login after register
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Đăng ký thành công! Xin chào ' + (user.get_full_name() or user.email))
                return redirect('home:index')
            else:
                messages.success(request, 'Đăng ký thành công. Vui lòng đăng nhập')
                return redirect('accounts:login')
    
    return render(request, 'accounts/register.html')


def forgot_password_view(request):
    """
    Trang quên mật khẩu
    """
    if request.user.is_authenticated:
        return redirect('home:index')
    
    if request.method == 'POST':
        email_or_phone = request.POST.get('email_or_phone', '').strip()
        
        if not email_or_phone:
            messages.error(request, 'Vui lòng nhập email hoặc số điện thoại')
            return render(request, 'accounts/forgot_password.html')
        
        # Tìm user theo email hoặc phone
        user = None
        
        if '@' in email_or_phone:
            user = User.objects.filter(email=email_or_phone, is_active=True).first()
        else:
            user = User.objects.filter(phone_number=email_or_phone, is_active=True).first()
        
        if user:
            # Reset password to 12345
            user.set_password('12345')
            user.save()
            messages.success(request, 'Mật khẩu mới của bạn là: 12345')
        else:
            messages.error(request, 'Không tìm thấy email hoặc số điện thoại trong hệ thống')
    
    return render(request, 'accounts/forgot_password.html')


@login_required
def profile_view(request):
    """
    Trang thông tin cá nhân
    """
    if request.method == 'POST':
        # Xử lý đổi mật khẩu
        if 'change_password' in request.POST:
            new_password = request.POST.get('new_password', '')
            confirm_password = request.POST.get('confirm_password', '')
            
            # Validate
            if not new_password or not confirm_password:
                messages.error(request, 'Vui lòng nhập đầy đủ thông tin mật khẩu')
            elif len(new_password) < 6:
                messages.error(request, 'Mật khẩu mới phải có ít nhất 6 ký tự')
            elif new_password != confirm_password:
                messages.error(request, 'Mật khẩu mới không khớp')
            else:
                # Cập nhật mật khẩu
                user = request.user
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Đổi mật khẩu thành công')
    
    return render(request, 'accounts/profile/profile.html')


def logout_view(request):
    """
    Đăng xuất
    """
    logout(request)
    messages.info(request, 'Đã đăng xuất')
    return redirect('home:index')
