/* ==================== AUTH JAVASCRIPT ==================== */

document.addEventListener('DOMContentLoaded', function() {
    
    // ==================== TOGGLE PASSWORD VISIBILITY ====================
    window.togglePassword = function(inputId) {
        const input = document.getElementById(inputId);
        const icon = document.getElementById(inputId + 'Icon');
        
        if (input && icon) {
            if (input.type === 'password') {
                input.type = 'text';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                input.type = 'password';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        }
    };
    
    // ==================== LOGIN FORM VALIDATION ====================
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value;
            
            if (!email || !password) {
                e.preventDefault();
                Toast.error('Vui lòng nhập đầy đủ email và mật khẩu');
                return false;
            }
            
            // Basic email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                e.preventDefault();
                Toast.error('Email không hợp lệ');
                return false;
            }
            
            return true;
        });
    }
    
    // ==================== REGISTER FORM VALIDATION ====================
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', function(e) {
            const fullName = document.getElementById('full_name').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone_number').value.trim();
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm_password').value;
            
            // Check required fields
            if (!fullName || !email || !phone || !password || !confirmPassword) {
                e.preventDefault();
                Toast.error('Vui lòng nhập đầy đủ thông tin');
                return false;
            }
            
            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                e.preventDefault();
                Toast.error('Email không hợp lệ');
                return false;
            }
            
            // Phone validation (Vietnamese phone number)
            const phoneRegex = /^0[0-9]{9}$/;
            if (!phoneRegex.test(phone)) {
                e.preventDefault();
                Toast.error('Số điện thoại không hợp lệ (phải bắt đầu bằng 0 và có 10 số)');
                return false;
            }
            
            // Password length
            if (password.length < 6) {
                e.preventDefault();
                Toast.error('Mật khẩu phải có ít nhất 6 ký tự');
                return false;
            }
            
            // Password match
            if (password !== confirmPassword) {
                e.preventDefault();
                Toast.error('Mật khẩu không khớp');
                return false;
            }
            
            return true;
        });
    }
    
    // ==================== FORGOT PASSWORD FORM VALIDATION ====================
    const forgotPasswordForm = document.getElementById('forgotPasswordForm');
    if (forgotPasswordForm) {
        forgotPasswordForm.addEventListener('submit', function(e) {
            const emailOrPhone = document.getElementById('email_or_phone').value.trim();
            
            if (!emailOrPhone) {
                e.preventDefault();
                Toast.error('Vui lòng nhập email hoặc số điện thoại');
                return false;
            }
            
            // Check if it's a valid email or phone format
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            const phoneRegex = /^0[0-9]{9,10}$/;
            
            if (!emailRegex.test(emailOrPhone) && !phoneRegex.test(emailOrPhone)) {
                e.preventDefault();
                Toast.error('Vui lòng nhập đúng định dạng email hoặc số điện thoại');
                return false;
            }
            
            return true;
        });
    }
    
    // ==================== HANDLE DJANGO MESSAGES (Toast from backend) ====================
    // Check if there are Django messages to display
    const djangoMessages = document.querySelectorAll('[data-django-message]');
    djangoMessages.forEach(function(msg) {
        const message = msg.dataset.djangoMessage;
        const tags = msg.dataset.djangoTags || 'info';
        
        if (tags.includes('error')) {
            Toast.error(message);
        } else if (tags.includes('success')) {
            Toast.success(message);
        } else if (tags.includes('warning')) {
            Toast.warning(message);
        } else {
            Toast.info(message);
        }
    });
});

