# Product API with MongoDB

This is a simple **Product API** built using **Django**, **Django Rest Framework (DRF)**, and **MongoDB**. It allows performing CRUD operations (Create, Read, Update, Delete) on product data stored in a MongoDB database. The application implements the **Repository Pattern** and the **Service Layer** for clear separation of concerns.

## Features
- **GET /products/**: List all products.
- **GET /products/{product_id}/**: Get a specific product by its ID.
- **POST /products/**: Create a new product.
- **PUT /products/{product_id}/**: Update an existing product.
- **DELETE /products/{product_id}/**: Delete a product.

## Technologies Used
- **Django 3.x**
- **Django Rest Framework (DRF)**
- **MongoDB** (via **MongoEngine**)
- **Python 3.x**

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/product_api.git
cd product_api
```

### 2. Create a Virtual Environment

Create a Python virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

For Windows:
```bash
venv\Scripts\activate
```
For macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up MongoDB

Ensure that MongoDB is installed and running on your local machine. If you don’t have MongoDB installed, follow the [official MongoDB installation guide](https://www.mongodb.com/docs/manual/installation/).

Make sure MongoDB is running on the default port **27017**.

### 5. Configure Django Settings

In `settings.py`, configure the MongoDB database connection:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
        'NAME': 'product_api_db',
    }
}

# MongoEngine settings
from mongoengine import connect
connect('product_api_db', host='localhost', port=27017)
```

### 6. Run Migrations

Since we are using MongoDB, no migrations are required. However, ensure the models are synced by running:

```bash
python manage.py migrate
```

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server should now be running at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

---

## API Endpoints

### 1. **GET /products/**
Retrieves a list of all products.

#### Example Response:
```json
[
    {
        "id": "product_id_1",
        "name": "Product 1",
        "description": "Product description",
        "price": 100.0
    },
    {
        "id": "product_id_2",
        "name": "Product 2",
        "description": "Product description",
        "price": 150.0
    }
]
```

### 2. **GET /products/{product_id}/**
Retrieves a product by its ID.

#### Example Response:
```json
{
    "id": "product_id_1",
    "name": "Product 1",
    "description": "Product description",
    "price": 100.0
}
```

### 3. **POST /products/**
Creates a new product.

#### Request Body:
```json
{
    "name": "New Product",
    "description": "Description of the new product",
    "price": 200.0
}
```

#### Example Response:
```json
{
    "id": "new_product_id",
    "name": "New Product",
    "description": "Description of the new product",
    "price": 200.0
}
```

### 4. **PUT /products/{product_id}/**
Updates an existing product by its ID.

#### Request Body:
```json
{
    "name": "Updated Product Name",
    "description": "Updated product description",
    "price": 250.0
}
```

#### Example Response:
```json
{
    "id": "product_id_1",
    "name": "Updated Product Name",
    "description": "Updated product description",
    "price": 250.0
}
```

### 5. **DELETE /products/{product_id}/**
Deletes a product by its ID.

#### Example Response:
```json
{
    "message": "Product deleted successfully"
}
```

---

## Service Layer and Repository Pattern

- **`ProductService`**: Contains all the business logic for handling products.
- **`ProductRepository`**: Handles MongoDB interactions and abstracts the data layer.

By following these design patterns, the application maintains a clean separation between data access, business logic, and presentation.

---

## Directory Structure

```bash
product_api/
│
├── products/
│   ├── migrations/                  # Migration files (not used with MongoDB)
│   ├── models.py                    # MongoDB Models
│   ├── serializers.py               # DRF Serializers
│   ├── service.py                   # Service Layer (Business Logic)
│   ├── repository.py                # Repository Layer (Database Access)
│   └── views.py                     # API Views
│
├── manage.py                        # Django management commands
└── requirements.txt                 # Project dependencies
```

---

## Testing the API with Postman

You can test all the API operations using **Postman** by sending HTTP requests to the respective endpoints:

- **GET /products/**: Fetch the list of all products.
- **GET /products/{product_id}/**: Get the details of a product by ID.
- **POST /products/**: Create a new product with required fields (name, description, price).
- **PUT /products/{product_id}/**: Update an existing product.
- **DELETE /products/{product_id}/**: Delete a product.

---

