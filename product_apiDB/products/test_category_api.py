# products/tests/test_category_api.py

from django.test import TestCase, RequestFactory
from products.models import ProductCategory
from products.views import ProductCategoryView
from bson import ObjectId

class ProductCategoryAPITest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @classmethod
    def setUpTestData(cls):
        cls.cat1 = ProductCategory(
            id=ObjectId(), title="Electronics", description="Electronic Items"
        )
        cls.cat1.save()

        cls.cat2 = ProductCategory(
            id=ObjectId(), title="Books", description="All kinds of books"
        )
        cls.cat2.save()

    def test_get_all_categories(self):
        request = self.factory.get('/products/categories/')
        response = ProductCategoryView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_post_category(self):
        data = {
            "title": "Furniture",
            "description": "Home and office furniture"
        }
        request = self.factory.post('/products/categories/', data, content_type="application/json")
        response = ProductCategoryView.as_view()(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], data["title"])
