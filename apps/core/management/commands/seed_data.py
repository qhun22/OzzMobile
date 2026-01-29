"""
Seed Data Command - Create sample data
Create sample data for Category and Product
"""
from django.core.management.base import BaseCommand
from apps.products.models import Category, Product


class Command(BaseCommand):
    """
    Command to create sample data
    Run: python manage.py seed_data
    """
    
    help = 'Create sample data for Category and Product'
    
    def handle(self, *args, **options):
        """
        Execute sample data creation
        """
        self.stdout.write(self.style.SUCCESS('=' * 50))
        self.stdout.write(self.style.SUCCESS('Starting to create sample data...'))
        self.stdout.write(self.style.SUCCESS('=' * 50))
        
        # Create Categories
        categories = self.create_categories()
        
        # Create Products
        products = self.create_products(categories)
        
        self.stdout.write(self.style.SUCCESS('=' * 50))
        self.stdout.write(self.style.SUCCESS('Successfully created!'))
        self.stdout.write(self.style.SUCCESS(f'  - Categories: {len(categories)}'))
        self.stdout.write(self.style.SUCCESS(f'  - Products: {len(products)}'))
        self.stdout.write(self.style.SUCCESS('=' * 50))
    
    def create_categories(self):
        """
        Create sample Category data
        """
        self.stdout.write('\n[1/2] Creating Categories...')
        
        categories_data = [
            {
                'name': 'iPhone',
                'slug': 'iphone',
                'description': 'Dien thoai iPhone chinh hang Apple',
                'order': 1,
            },
            {
                'name': 'Samsung',
                'slug': 'samsung',
                'description': 'Dien thoai Samsung Galaxy',
                'order': 2,
            },
            {
                'name': 'Xiaomi',
                'slug': 'xiaomi',
                'description': 'Dien thoai Xiaomi Redmi va Poco',
                'order': 3,
            },
            {
                'name': 'OPPO',
                'slug': 'oppo',
                'description': 'Dien thoai OPPO Reno va A-series',
                'order': 4,
            },
            {
                'name': 'Phu kien',
                'slug': 'phu-kien',
                'description': 'Phu kien dien thoai: op lung, sac, tai nghe',
                'order': 5,
            },
        ]
        
        categories = []
        for data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=data['slug'],
                defaults=data
            )
            if created:
                self.stdout.write(f'  + Created: {category.name}')
            else:
                self.stdout.write(f'  - Existed: {category.name}')
            categories.append(category)
        
        self.stdout.write(self.style.SUCCESS(f'  Total: {len(categories)} categories'))
        return categories
    
    def create_products(self, categories):
        """
        Create sample Product data
        """
        self.stdout.write('\n[2/2] Creating Products...')
        
        # Create dictionary for easy category access
        cat_dict = {c.slug: c for c in categories}
        
        products_data = [
            # iPhone products
            {
                'name': 'iPhone 16 Pro Max 256GB',
                'slug': 'iphone-16-pro-max-256gb',
                'category': cat_dict['iphone'],
                'short_description': 'iPhone 16 Pro Max - Sieu pham moi nhat tu Apple',
                'description': 'iPhone 16 Pro Max voi chip A18 Pro, man hinh Super Retina XDR 6.9 inch, camera 48MP.',
                'price': 34990000,
                'original_price': 36990000,
                'stock': 50,
                'sku': 'IP16PM256',
                'is_featured': True,
                'specifications': {
                    'Man hinh': '6.9 inch Super Retina XDR',
                    'Chip': 'A18 Pro',
                    'RAM': '8GB',
                    'Bo nho': '256GB',
                    'Pin': '4685mAh',
                    'Camera': '48MP + 12MP + 12MP',
                },
            },
            {
                'name': 'iPhone 16 Pro 128GB',
                'slug': 'iphone-16-pro-128gb',
                'category': cat_dict['iphone'],
                'short_description': 'iPhone 16 Pro - Hieu nang dinh cao',
                'description': 'iPhone 16 Pro voi thiet ke titan, chip A18 Pro, he thong camera chuyen nghiep.',
                'price': 28990000,
                'original_price': 30990000,
                'stock': 30,
                'sku': 'IP16P128',
                'is_featured': True,
                'specifications': {
                    'Man hinh': '6.3 inch Super Retina XDR',
                    'Chip': 'A18 Pro',
                    'RAM': '8GB',
                    'Bo nho': '128GB',
                    'Pin': '3582mAh',
                    'Camera': '48MP + 48MP + 12MP',
                },
            },
            {
                'name': 'iPhone 15 128GB',
                'slug': 'iphone-15-128gb',
                'category': cat_dict['iphone'],
                'short_description': 'iPhone 15 - Dynamic Island, USB-C',
                'description': 'iPhone 15 voi Dynamic Island, camera 48MP, cong USB-C.',
                'price': 19990000,
                'original_price': 22990000,
                'stock': 100,
                'sku': 'IP15128',
                'specifications': {
                    'Man hinh': '6.1 inch Super Retina XDR',
                    'Chip': 'A16 Bionic',
                    'RAM': '6GB',
                    'Bo nho': '128GB',
                    'Pin': '3349mAh',
                    'Camera': '48MP + 12MP',
                },
            },
            {
                'name': 'iPhone 14 128GB',
                'slug': 'iphone-14-128gb',
                'category': cat_dict['iphone'],
                'short_description': 'iPhone 14 - Hieu nang on dinh',
                'description': 'iPhone 14 voi chip A15 Bionic, camera 12MP, notch truyen thong.',
                'price': 14990000,
                'stock': 80,
                'sku': 'IP14128',
                'specifications': {
                    'Man hinh': '6.1 inch Super Retina XDR',
                    'Chip': 'A15 Bionic',
                    'RAM': '6GB',
                    'Bo nho': '128GB',
                    'Pin': '3279mAh',
                    'Camera': '12MP + 12MP',
                },
            },
            # Samsung products
            {
                'name': 'Samsung Galaxy S24 Ultra 256GB',
                'slug': 'samsung-galaxy-s24-ultra-256gb',
                'category': cat_dict['samsung'],
                'short_description': 'Samsung S24 Ultra - Vu Android',
                'description': 'Samsung Galaxy S24 Ultra voi S Pen, chip Snapdragon 8 Gen 3, camera 200MP.',
                'price': 31990000,
                'original_price': 34990000,
                'stock': 45,
                'sku': 'S24U256',
                'is_featured': True,
                'specifications': {
                    'Man hinh': '6.8 inch QHD+ Dynamic AMOLED 2X',
                    'Chip': 'Snapdragon 8 Gen 3',
                    'RAM': '12GB',
                    'Bo nho': '256GB',
                    'Pin': '5000mAh',
                    'Camera': '200MP + 50MP + 12MP',
                },
            },
            {
                'name': 'Samsung Galaxy S24+ 256GB',
                'slug': 'samsung-galaxy-s24-plus-256gb',
                'category': cat_dict['samsung'],
                'short_description': 'Samsung S24+ - Man hinh lon',
                'description': 'Samsung Galaxy S24+ voi man hinh 6.7 inch, chip Exynos 2400.',
                'price': 24990000,
                'stock': 35,
                'sku': 'S24P256',
                'specifications': {
                    'Man hinh': '6.7 inch QHD+ Dynamic AMOLED 2X',
                    'Chip': 'Exynos 2400',
                    'RAM': '12GB',
                    'Bo nho': '256GB',
                    'Pin': '4900mAh',
                    'Camera': '50MP + 12MP + 10MP',
                },
            },
            {
                'name': 'Samsung Galaxy Z Fold 5 256GB',
                'slug': 'samsung-galaxy-z-fold-5-256gb',
                'category': cat_dict['samsung'],
                'short_description': 'Samsung Z Fold 5 - Dien thoai gap',
                'description': 'Samsung Galaxy Z Fold 5 voi man hinh gap 7.6 inch, S Pen.',
                'price': 39990000,
                'stock': 20,
                'sku': 'ZF5256',
                'is_featured': True,
                'specifications': {
                    'Man hinh': '7.6 inch Foldable Dynamic AMOLED 2X',
                    'Chip': 'Snapdragon 8 Gen 2',
                    'RAM': '12GB',
                    'Bo nho': '256GB',
                    'Pin': '4400mAh',
                    'Camera': '50MP + 12MP + 10MP',
                },
            },
            # Xiaomi products
            {
                'name': 'Xiaomi 14 Ultra 512GB',
                'slug': 'xiaomi-14-ultra-512gb',
                'category': cat_dict['xiaomi'],
                'short_description': 'Xiaomi 14 Ultra - Camera Leica',
                'description': 'Xiaomi 14 Ultra voi ong kinh Leica, chip Snapdragon 8 Gen 3.',
                'price': 29990000,
                'original_price': 32990000,
                'stock': 25,
                'sku': 'MI14U512',
                'is_featured': True,
                'specifications': {
                    'Man hinh': '6.73 inch WQHD+ LTPO AMOLED',
                    'Chip': 'Snapdragon 8 Gen 3',
                    'RAM': '16GB',
                    'Bo nho': '512GB',
                    'Pin': '5000mAh',
                    'Camera': '50MP + 50MP + 50MP + 50MP',
                },
            },
            {
                'name': 'Redmi Note 13 Pro 5G 256GB',
                'slug': 'redmi-note-13-pro-5g-256gb',
                'category': cat_dict['xiaomi'],
                'short_description': 'Redmi Note 13 Pro - King of Mid-range',
                'description': 'Redmi Note 13 Pro voi camera 200MP, man hinh 120Hz.',
                'price': 7990000,
                'original_price': 8990000,
                'stock': 150,
                'sku': 'RN13P256',
                'specifications': {
                    'Man hinh': '6.67 inch 1.5K OLED 120Hz',
                    'Chip': 'Snapdragon 7s Gen 2',
                    'RAM': '8GB',
                    'Bo nho': '256GB',
                    'Pin': '5100mAh',
                    'Camera': '200MP + 8MP + 2MP',
                },
            },
            {
                'name': 'POCO X6 Pro 512GB',
                'slug': 'poco-x6-pro-512gb',
                'category': cat_dict['xiaomi'],
                'short_description': 'POCO X6 Pro - Hieu nang cao',
                'description': 'POCO X6 Pro voi chip Dimensity 8300 Ultra, sac 67W.',
                'price': 9990000,
                'stock': 80,
                'sku': 'POX6P512',
                'specifications': {
                    'Man hinh': '6.67 inch 1.5K OLED 120Hz',
                    'Chip': 'Dimensity 8300 Ultra',
                    'RAM': '12GB',
                    'Bo nho': '512GB',
                    'Pin': '5000mAh',
                    'Camera': '64MP + 8MP + 2MP',
                },
            },
            # OPPO products
            {
                'name': 'OPPO Find X7 Ultra 256GB',
                'slug': 'oppo-find-x7-ultra-256gb',
                'category': cat_dict['oppo'],
                'short_description': 'OPPO Find X7 Ultra - Camera 1 inch',
                'description': 'OPPO Find X7 Ultra voi camera 1 inch, Hasselblad, chip Snapdragon 8 Gen 3.',
                'price': 28990000,
                'stock': 30,
                'sku': 'OPX7U256',
                'is_featured': True,
                'specifications': {
                    'Man hinh': '6.82 inch 2K LTPO AMOLED',
                    'Chip': 'Snapdragon 8 Gen 3',
                    'RAM': '16GB',
                    'Bo nho': '256GB',
                    'Pin': '5000mAh',
                    'Camera': '50MP + 50MP + 50MP + 50MP',
                },
            },
            {
                'name': 'OPPO Reno12 Pro 5G 256GB',
                'slug': 'oppo-reno12-pro-5g-256gb',
                'category': cat_dict['oppo'],
                'short_description': 'OPPO Reno12 Pro - AI Phone',
                'description': 'OPPO Reno12 Pro voi tinh nang AI, thiet ke mong nhe.',
                'price': 14990000,
                'stock': 60,
                'sku': 'OPR12P256',
                'specifications': {
                    'Man hinh': '6.7 inch FHD+ AMOLED 120Hz',
                    'Chip': 'Dimensity 7300 Energy',
                    'RAM': '12GB',
                    'Bo nho': '256GB',
                    'Pin': '5000mAh',
                    'Camera': '50MP + 50MP + 8MP',
                },
            },
            # Phu kien
            {
                'name': 'Cap sac nhanh Anker 100W',
                'slug': 'cap-sac-nhanh-anker-100w',
                'category': cat_dict['phu-kien'],
                'short_description': 'Cap USB-C to USB-C 100W',
                'description': 'Cap sac nhanh Anker PowerLine III, cong suat 100W, dai 1.8m.',
                'price': 590000,
                'stock': 200,
                'sku': 'ANK100WC',
                'specifications': {
                    'Loai': 'USB-C to USB-C',
                    'Cong suat': '100W',
                    'Chieu dai': '1.8m',
                    'Chat lieu': 'Vai ben',
                },
            },
            {
                'name': 'Tai nghe AirPods Pro 2 USB-C',
                'slug': 'tai-nghe-airpods-pro-2-usb-c',
                'category': cat_dict['phu-kien'],
                'short_description': 'Tai nghe AirPods Pro 2 voi cong USB-C',
                'description': 'Tai nguyen Apple AirPods Pro 2 voi USB-C, Active Noise Cancellation.',
                'price': 5990000,
                'stock': 100,
                'sku': 'APP2C',
                'is_featured': True,
                'specifications': {
                    'Loai': 'In-ear True Wireless',
                    'ANC': 'Co',
                    'Pin': '6 gio (listening)',
                    'Sac': 'USB-C',
                },
            },
        ]
        
        products = []
        for data in products_data:
            product, created = Product.objects.get_or_create(
                sku=data['sku'],
                defaults=data
            )
            if created:
                self.stdout.write(f'  + Created: {product.name}')
            else:
                self.stdout.write(f'  - Existed: {product.name}')
            products.append(product)
        
        self.stdout.write(self.style.SUCCESS(f'  Total: {len(products)} products'))
        return products
