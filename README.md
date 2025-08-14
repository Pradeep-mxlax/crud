# Django E-commerce

A minimal e-commerce site built with Django. Features:

- Product catalog with categories
- Session-based shopping cart
- Checkout flow creating orders
- User registration/login via Django auth
- Admin management for products and orders

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Create project (already done by scripts)

```bash
django-admin startproject ecommerce .
python manage.py startapp catalog
python manage.py startapp cart
python manage.py startapp orders
python manage.py startapp accounts
```

## Run

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

Open http://localhost:8000/

## Notes

- Uses SQLite by default.
- To enable product images, ensure `media/` exists and configure a media root.