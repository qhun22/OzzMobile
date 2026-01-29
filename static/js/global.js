/* QHUN22 Mobile - Global JavaScript Utilities */

// Toast notification system
const Toast = {
    show(message, type = 'info', duration = 4000) {
        const container = document.getElementById('toast-container') || this.createContainer();
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.textContent = message;
        container.appendChild(toast);
        
        setTimeout(() => toast.remove(), duration);
    },
    
    createContainer() {
        const container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'fixed top-4 right-4 z-50 flex flex-col gap-3';
        document.body.appendChild(container);
        return container;
    },
    
    success(message) { this.show(message, 'success'); },
    error(message) { this.show(message, 'error'); },
    warning(message) { this.show(message, 'warning'); },
    info(message) { this.show(message, 'info'); }
};

// Modal system
const Modal = {
    open(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) modal.classList.remove('hidden');
    },
    
    close(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) modal.classList.add('hidden');
    },
    
    init() {
        document.querySelectorAll('[data-modal-target]').forEach(button => {
            button.addEventListener('click', () => {
                this.open(button.dataset.modalTarget);
            });
        });
        
        document.querySelectorAll('[data-modal-close]').forEach(button => {
            button.addEventListener('click', () => {
                const modal = button.closest('[id^="modal-"]');
                if (modal) this.close(modal.id);
            });
        });
    }
};

// Format currency (VND)
function formatCurrency(amount) {
    return new Intl.NumberFormat('vi-VN', {
        style: 'currency',
        currency: 'VND'
    }).format(amount);
}

// Debounce utility
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// API fetch wrapper
async function apiFetch(url, options = {}) {
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
        },
    };
    
    const response = await fetch(url, { ...defaultOptions, ...options });
    
    if (!response.ok) {
        const error = await response.json().catch(() => ({ message: 'Lỗi không xác định' }));
        throw new Error(error.message || 'Lỗi kết nối');
    }
    
    return response.json();
}

// Initialize global utilities
document.addEventListener('DOMContentLoaded', () => {
    Modal.init();
});

