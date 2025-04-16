# products/tests/test_product_api.py

from django.test import TestCase, RequestFactory
from models import Product
from views import ProductListView, ProductDetailView
from bson import ObjectId

class ProductAPITest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @classmethod
    def setUpTestData(cls):
        cls.product1 = Product(
            id=ObjectId(), name="Laptop", description="Gaming Laptop", price=1200, brand="HP"
        )
        cls.product1.save()

        cls.product2 = Product(
            id=ObjectId(), name="Phone", description="Smartphone", price=800, brand="Samsung"
        )
        cls.product2.save()

    def test_get_all_products(self):
        request = self.factory.get('/products/')
        response = ProductListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_post_product(self):
        data = {
            "name": "Tablet",
            "description": "Android tablet",
            "price": 500,
            "brand": "Lenovo"
        }
        request = self.factory.post('/products/', data, content_type="application/json")
        response = ProductListView.as_view()(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], data["name"])

    def test_get_product_by_id(self):
        request = self.factory.get(f'/products/{str(self.product1.id)}/')
        response = ProductDetailView.as_view()(request, product_id=str(self.product1.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.product1.name)

    def test_update_product(self):
        data = {
            "name": "Laptop Pro",
            "description": "Updated",
            "price": 1300
        }
        request = self.factory.put(
            f'/products/{str(self.product1.id)}/', data, content_type="application/json"
        )
        response = ProductDetailView.as_view()(request, product_id=str(self.product1.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Laptop Pro")

    def test_delete_product(self):
        request = self.factory.delete(f'/products/{str(self.product2.id)}/')
        response = ProductDetailView.as_view()(request, product_id=str(self.product2.id))
        self.assertEqual(response.status_code, 204)
