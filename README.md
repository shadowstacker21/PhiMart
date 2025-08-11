# 📦 PhiMart – E-commerce API

PhiMart is a **Django REST Framework (DRF)**-based e-commerce backend API that provides endpoints for managing products, categories, orders, and carts. It includes **JWT authentication** via **Djoser** and interactive **API documentation** using **drf_yasg (Swagger UI)**.

---

## 🚀 Features

- **Product Management** – List, create, update, and delete products.
- **Category Management** – Organize products into categories.
- **Cart System** – Add, update, and remove items from the cart.
- **Order Management** – Place and view customer orders.
- **User Authentication** – JWT-based authentication using **Djoser**.
- **API Documentation** – Swagger UI and ReDoc integration with **drf_yasg**.
- **RESTful Design** – Clean and consistent API design following DRF best practices.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** Djoser + JWT (SimpleJWT)
- **Documentation:** drf_yasg (Swagger / ReDoc)
- **Database:** SQLite / PostgreSQL (configurable)
- **Python Version:** 3.10+

---

## 📂 Project Structure

```
PhiMart/
│── manage.py
│── requirements.txt
│── README.md
│
├── phismart/                # Project settings
├── products/                # Product & category APIs
├── orders/                  # Order APIs
├── carts/                    # Cart APIs
├── users/                   # User registration & authentication
└── ...
```

---

## 🔑 API Endpoints

### Authentication (Djoser + JWT)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/auth/jwt/create/` | Obtain JWT tokens |
| POST   | `/auth/jwt/refresh/` | Refresh JWT token |
| POST   | `/auth/jwt/verify/`  | Verify JWT token |
| POST   | `/auth/users/`       | Register new user |
| GET    | `/auth/users/me/`    | Get logged-in user profile |

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/products/`        | List all products |
| POST   | `/api/products/`        | Create a product |
| GET    | `/api/products/{id}/`   | Retrieve a product |
| PUT    | `/api/products/{id}/`   | Update a product |
| DELETE | `/api/products/{id}/`   | Delete a product |

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/categories/`      | List categories |
| POST   | `/api/categories/`      | Create category |

### Carts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/carts/`            | Retrieve cart |
| POST   | `/api/carts/add/`        | Add product to cart |
| DELETE | `/api/carts/remove/`     | Remove product from cart |

### Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/orders/`          | List orders |
| POST   | `/api/orders/`          | Create new order |

---

## 📜 API Documentation

- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)  
- **ReDoc:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## ⚙️ Installation & Setup

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/phimart.git
cd phimart
```

2️⃣ **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Run Migrations**
```bash
python manage.py migrate
```

5️⃣ **Create Superuser**
```bash
python manage.py createsuperuser
```

6️⃣ **Run Development Server**
```bash
python manage.py runserver
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and set:
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST = your_email_host
```

---

## 📌 Requirements

See [requirements.txt](./requirements.txt) for full dependency list.

---

## 📄 License

This project is licensed under the **MIT License**.
