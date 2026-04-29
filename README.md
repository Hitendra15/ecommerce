# 🛒 MyShop – E-commerce Website

A modern **E-commerce Web Application** built with **Django**.
Includes authentication, product search, cart system, checkout, and order management.

---

## 🚀 Features

* 🔐 User Authentication (Register, Login, Logout, Forgot password)
* 📧 Email Verification
* 🛍️ Product Listing & Search
* 🛒 Cart Management
* 📦 Checkout System
* 🏠 Address Management
* 📄 Order Placement
* 🔔 Toast Notifications
* 📱 Responsive UI (Bootstrap)

---

## 🧰 Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS, Bootstrap, jQuery
* **Database:** PostgreSQL
* **Auth:** Django Authentication System

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/Hitendra15/ecommerce.git
cd ecommerce
```

---

### 2. Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

```bash
# Windows
env\Scripts\activate

# Mac/Linux
source env/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup PostgreSQL

Make sure PostgreSQL is installed and running.

Create database:

```sql
CREATE DATABASE ecommerce_db;
```

---

### 5. Create `.env` File

Create a `.env` file in your project root:

```env
DB_NAME=ecommerce_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 6. Install dotenv

```bash
pip install python-dotenv
```

---

### 7. Update `settings.py`

```python
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=BASE_DIR / '.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

---

### 8. Run Migrations

```bash
python manage.py migrate
```

---

### 9. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 10. Run Server

```bash
python manage.py runserver
```

👉 Open: http://127.0.0.1:8000/

---

## 📁 Project Structure

```
ecommerce/
│── core/templates/core                 # Base templates (header, footer, sidebar)
│── product/                            # Product logic
│── user/                               # Authentication
│── order/                              # Orders, checkout
│── cart/                               # Cart (store product in session)
│── core/static/core                    # CSS, JS
│── project_app/templates/              # HTML templates
│── media/products/                     # images (default product images)
```

---

## 🔍 Search Feature

Search products via header:

```
/?q=laptop
```

---

## 📦 Checkout Flow

1. Add product to cart
2. Go to checkout
3. Add/select address
4. Click **Complete Order**
5. Order saved

---

## 🔐 Authentication Flow

* Register
* Email verification
* Login
* Logout
* Forgot password

---

## ⚠️ Important

Add `.env` to `.gitignore`:

```bash
.env
```

👉 Prevents exposing sensitive data

---

## 🚀 Future Improvements

* 💳 Payment Integration (Razorpay / Stripe)
* 📦 Order Tracking
* ❤️ Wishlist
* ⭐ Reviews
* 🔎 Live Search

---

## 🤝 Contributing

Pull requests are welcome.

---

## 👨‍💻 Author

**Hitendra**
GitHub: https://github.com/Hitendra15
