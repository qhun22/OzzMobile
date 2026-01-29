// QHUN22 Mobile - API Wrapper

const API_BASE = '/api';

// Auth API
const AuthAPI = {
    async login(email, password) {
        return apiFetch(`${API_BASE}/auth/login/`, {
            method: 'POST',
            body: JSON.stringify({ email, password })
        });
    },
    
    async register(data) {
        return apiFetch(`${API_BASE}/auth/register/`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    },
    
    async logout() {
        return apiFetch(`${API_BASE}/auth/logout/`, { method: 'POST' });
    },
    
    async checkAuth() {
        return apiFetch(`${API_BASE}/auth/check/`);
    }
};

// Cart API
const CartAPI = {
    async getCart() {
        return apiFetch(`${API_BASE}/cart/`);
    },
    
    async addItem(productId, quantity = 1) {
        return apiFetch(`${API_BASE}/cart/add/`, {
            method: 'POST',
            body: JSON.stringify({ product_id: productId, quantity })
        });
    },
    
    async updateItem(itemId, quantity) {
        return apiFetch(`${API_BASE}/cart/update/`, {
            method: 'POST',
            body: JSON.stringify({ item_id: itemId, quantity })
        });
    },
    
    async removeItem(itemId) {
        return apiFetch(`${API_BASE}/cart/remove/`, {
            method: 'POST',
            body: JSON.stringify({ item_id: itemId })
        });
    },
    
    async clearCart() {
        return apiFetch(`${API_BASE}/cart/clear/`, { method: 'POST' });
    }
};

// Product API
const ProductAPI = {
    async list(params = {}) {
        const query = new URLSearchParams(params).toString();
        return apiFetch(`${API_BASE}/products/${query ? '?' + query : ''}`);
    },
    
    async getDetail(slug) {
        return apiFetch(`${API_BASE}/products/${slug}/`);
    },
    
    async search(query) {
        return apiFetch(`${API_BASE}/products/search/?q=${encodeURIComponent(query)}`);
    }
};

// Order API
const OrderAPI = {
    async create(data) {
        return apiFetch(`${API_BASE}/orders/create/`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    },
    
    async list() {
        return apiFetch(`${API_BASE}/orders/`);
    },
    
    async getDetail(orderId) {
        return apiFetch(`${API_BASE}/orders/${orderId}/`);
    },
    
    async cancel(orderId, reason) {
        return apiFetch(`${API_BASE}/orders/${orderId}/cancel/`, {
            method: 'POST',
            body: JSON.stringify({ reason })
        });
    }
};

// Review API
const ReviewAPI = {
    async create(data) {
        return apiFetch(`${API_BASE}/reviews/`, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    },
    
    async getByProduct(productId) {
        return apiFetch(`${API_BASE}/products/${productId}/reviews/`);
    }
};

