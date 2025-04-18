import unittest
from django.test import Client
import json

class TestProductIntegration(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.base_url_products = "/products/"

    def test_create_product(self):
        product_data = {
            "name": "iPhone",
            "description": "Great camera and performance",
            "price": 70000,
            "brand": "Apple",
            "quantity": 5,
            "category": {
                "title": "Electronics",
                "description": "Gadgets and devices"
            }
        }

        response = self.client.post(
            self.base_url_products,
            json.dumps(product_data),
            content_type="application/json"
        )

        print("Create Product Response:", response.status_code, response.json())

        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    def test_get_product(self):
        # First, create a product
        product_data = {
            "name": "iPhone",
            "description": "Great camera and performance",
            "price": 70000,
            "brand": "Apple",
            "quantity": 5,
            "category": {
                "title": "Electronics",
                "description": "Gadgets and devices"
            }
        }

        create_response = self.client.post(
            self.base_url_products,
            json.dumps(product_data),
            content_type="application/json"
        )
        self.assertEqual(create_response.status_code, 201)
        product_id = create_response.json()["id"]

        # Then retrieve the product
        response = self.client.get(f"{self.base_url_products}{product_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], product_id)

    def test_list_products(self):
        response = self.client.get(self.base_url_products)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
