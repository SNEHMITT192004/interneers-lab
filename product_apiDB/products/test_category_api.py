import unittest
from django.test import Client
import json


class TestCategoryIntegration(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.category_url = "/products/categories/"

    def test_create_category(self):
        category_data = {
            "title": "Electronics",
            "description": "Gadgets and devices"
        }

        response = self.client.post(
            self.category_url,
            json.dumps(category_data),
            content_type="application/json"
        )

        print("Create Category Response:", response.status_code, response.json())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], "Electronics")

    def test_list_categories(self):
        # Create one category first
        category_data = {
            "title": "Electronics",
            "description": "Gadgets and devices"
        }

        create_response = self.client.post(
            self.category_url,
            json.dumps(category_data),
            content_type="application/json"
        )
        self.assertEqual(create_response.status_code, 201)

        # Now list all categories
        list_response = self.client.get(self.category_url)
        print("List Categories Response:", list_response.status_code, list_response.json())

        self.assertEqual(list_response.status_code, 200)
        self.assertIsInstance(list_response.json(), list)
        self.assertGreaterEqual(len(list_response.json()), 1)
