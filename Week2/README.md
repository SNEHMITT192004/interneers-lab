# Product API - Django REST Framework

## 📌 Overview
This project is a **Django REST Framework (DRF) API** for managing products in an inventory system. It provides **CRUD (Create, Read, Update, Delete) operations** on products, using in-memory operations.

---

## 🚀 Features
- Create, retrieve, update, and delete products.
- Uses **Django REST Framework (DRF)** for API development.
- In-memory storage (No database used).
- Input **validations** to ensure data integrity.
- Well-structured **serializers** for data conversion.
- **ViewSets and Routers** for simplified API routing.

---

## 📂 Project Structure
```
product_api/
│── product_api/         # Main project folder
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL configuration
│── products/            # App for managing products
│   ├── models.py        # Product model (if using DB in future)
│   ├── serializers.py   # Serializers to convert models to JSON
│   ├── views.py         # API views using ViewSets
│   ├── urls.py          # URL routing for products
│── requirements.txt     # Project dependencies
│── manage.py            # Django CLI tool
```

---

## 🛠️ Technologies Used
- **Python 3.x**
- **Django 4.x**
- **Django REST Framework (DRF)**

---

## 🏗️ Setup & Installation
Follow these steps to set up the project on your local machine:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/SNEHMITT192004/interneers-lab.git
cd interneers-lab/product_api
```

### 2️⃣ Create & Activate a Virtual Environment
```sh
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Django Server
```sh
python manage.py runserver
```
Now, open **http://127.0.0.1:8000/** in your browser.

---

## 🔗 API Endpoints
| Method | Endpoint          | Description               |
|--------|------------------|---------------------------|
| GET    | `/products/`      | Get all products         |
| POST   | `/products/`      | Create a new product     |
| GET    | `/products/{id}/` | Get a specific product   |
| PUT    | `/products/{id}/` | Update a product        |
| DELETE | `/products/{id}/` | Delete a product        |

---

## 🛡️ Validations Used
| Field       | Validation Applied                          |
|------------|------------------------------------------|
| `name`     | Required, max 200 characters           |
| `price`    | Required, must be positive             |
| `category` | Required, must be a valid choice       |
| `brand`    | Required, max 100 characters           |
| `quantity` | Required, must be a non-negative value |

---

## 🔬 Testing APIs with Postman / cURL
### Option 1: Using cURL
#### Create a Product (POST)
```sh
curl -X POST http://127.0.0.1:8000/products/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Laptop", "category": "Electronics", "price": 75000, "brand": "Dell", "quantity": 10}'
```

#### Get All Products (GET)
```sh
curl -X GET http://127.0.0.1:8000/products/
```

#### Update a Product (PUT)
```sh
curl -X PUT http://127.0.0.1:8000/products/1/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Gaming Laptop", "price": 90000}'
```

#### Delete a Product (DELETE)
```sh
curl -X DELETE http://127.0.0.1:8000/products/1/
```

### Option 2: Using Postman
1. Open **Postman**.
2. Set URL to **http://127.0.0.1:8000/products/**.
3. Choose Method (**POST, GET, PUT, DELETE**).
4. For **POST/PUT** requests:
   - Select **Body → raw → JSON**.
   - Enter the following:

```json
{
    "name": "Laptop",
    "description": "A gaming laptop",
    "category": "Electronics",
    "price": 1200.50,
    "brand": "Asus",
    "quantity": 10
}
```
5. Click **Send** and check responses.

---

## 🎯 Future Enhancements
- Add **Database support** using PostgreSQL.
- Implement **JWT Authentication**.
- Enable **Pagination & Filtering**.

---

## 👨‍💻 Author
**Sneha Mittal**  

---

🚀 **Happy Coding!**

