/* ==================== PROFILE JAVASCRIPT ==================== */

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
    
    // ==================== PASSWORD CHANGE FORM VALIDATION ====================
    const changePasswordForm = document.getElementById('changePasswordForm');
    if (changePasswordForm) {
        changePasswordForm.addEventListener('submit', function(e) {
            const newPassword = document.getElementById('new_password').value;
            const confirmPassword = document.getElementById('confirm_password').value;
            
            // Validate required fields
            if (!newPassword || !confirmPassword) {
                e.preventDefault();
                Toast.error('Vui lòng nhập đầy đủ thông tin mật khẩu');
                return false;
            }
            
            // Password length validation
            if (newPassword.length < 6) {
                e.preventDefault();
                Toast.error('Mật khẩu mới phải có ít nhất 6 ký tự');
                return false;
            }
            
            // Password match validation
            if (newPassword !== confirmPassword) {
                e.preventDefault();
                Toast.error('Mật khẩu mới không khớp');
                return false;
            }
            
            return true;
        });
    }
    
    // ==================== LOGOUT CONFIRMATION ====================
    const logoutLink = document.querySelector('.logout-section a[href*="logout"]');
    if (logoutLink) {
        logoutLink.addEventListener('click', function(e) {
            // Optional: Add confirmation for older users
            // Uncomment below if needed:
            // if (!confirm('Bạn có chắc chắn muốn đăng xuất?')) {
            //     e.preventDefault();
            // }
        });
    }
});

