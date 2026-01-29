# QHUN22 Mobile Project Structure

## Cấu trúc thư mục

```
D:\Py\Ozz\
├── config/                  # Cấu hình Django
│   ├── __init__.py
│   ├── settings.py          # Import settings môi trường
│   ├── base.py              # Cài đặt chung
│   ├── local.py             # Cài đặt development
│   ├── production.py        # Cài đặt production
│   ├── urls.py              # Root URL config
│   └── wsgi.py              # WSGI config
├── apps/                    # Django Apps
│   ├── core/                # Ứng dụng cốt lõi (utils, mixins, context processors)
│   ├── accounts/            # Xác thực và quản lý user
│   ├── products/            # Sản phẩm và danh mục
│   ├── cart/                # Giỏ hàng
│   ├── orders/              # Đơn hàng
│   ├── reviews/             # Đánh giá sản phẩm
│   ├── promotions/          # Khuyến mãi và coupon
│   ├── payments/            # Thanh toán
│   └── home/                # Trang chủ
├── static/                  # Static files (CSS, JS, images)
├── templates/               # Django templates
├── media/                   # User uploaded files
├── logs/                    # Log files
├── scripts/                 # Deployment scripts
├── locale/                  # Translation files
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

## Chạy dự án

```bash
# Tạo môi trường ảo
python -m venv venv
.\venv\Scripts\activate

# Cài đặt dependencies
pip install -r requirements.txt

# Tạo .env từ .env.example
copy .env.example .env

# Chạy migrations
python manage.py migrate

# Tạo superuser
python manage.py createsuperuser

# Chạy server
python manage.py runserver
```
