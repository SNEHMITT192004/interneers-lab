import unittest
from unittest.mock import patch, MagicMock
from service import ProductService, ProductCategoryService
from models import Product, ProductCategory

class ProductServiceTestCase(unittest.TestCase):

    @patch("service.Product.objects")
    def test_get_all_products(self, mock_product_objects):
        mock_product_objects.all.return_value = [MagicMock(), MagicMock()]
        products = ProductService.get_all_products()
        self.assertEqual(len(products), 2)
        mock_product_objects.all.assert_called_once()

    @patch("service.Product.objects")
    def test_get_product_by_id_found(self, mock_product_objects):
        mock_product = MagicMock()
        mock_product_objects.get.return_value = mock_product
        result = ProductService.get_product_by_id("someid")
        self.assertEqual(result, mock_product)
        mock_product_objects.get.assert_called_once_with(id="someid")

    @patch("service.Product.objects")
    def test_get_product_by_id_not_found(self, mock_product_objects):
        mock_product_objects.get.side_effect = Product.DoesNotExist
        result = ProductService.get_product_by_id("missing-id")
        self.assertIsNone(result)

    @patch("service.Product")
    def test_create_product(self, mock_product_class):
        mock_product = MagicMock()
        mock_product_class.return_value = mock_product
        result = ProductService.create_product("Laptop", "Desc", 1000, "HP")
        mock_product.save.assert_called_once()
        self.assertEqual(result, mock_product)

    @patch.object(ProductService, "get_product_by_id")
    def test_update_product_found(self, mock_get_product):
        mock_product = MagicMock()
        mock_get_product.return_value = mock_product
        updated = ProductService.update_product("id", "NewName", "NewDesc", 1500)
        self.assertEqual(updated.name, "NewName")
        mock_product.save.assert_called_once()

    @patch.object(ProductService, "get_product_by_id")
    def test_update_product_not_found(self, mock_get_product):
        mock_get_product.return_value = None
        result = ProductService.update_product("id", "New", "New", 1200)
        self.assertIsNone(result)

    @patch.object(ProductService, "get_product_by_id")
    def test_delete_product_success(self, mock_get_product):
        mock_product = MagicMock()
        mock_get_product.return_value = mock_product
        result = ProductService.delete_product("someid")
        mock_product.delete.assert_called_once()
        self.assertTrue(result)

    @patch.object(ProductService, "get_product_by_id")
    def test_delete_product_failure(self, mock_get_product):
        mock_get_product.return_value = None
        result = ProductService.delete_product("missing-id")
        self.assertFalse(result)


class ProductCategoryServiceTestCase(unittest.TestCase):

    @patch("service.ProductCategory.objects")
    def test_get_all_categories(self, mock_category_objects):
        mock_category_objects.all.return_value = [MagicMock(), MagicMock()]
        result = ProductCategoryService.get_all_categories()
        self.assertEqual(len(result), 2)
        mock_category_objects.all.assert_called_once()

    @patch("service.ProductCategory")
    def test_create_category(self, mock_category_class):
        mock_category = MagicMock()
        mock_category_class.return_value = mock_category
        result = ProductCategoryService.create_category("Electronics", "desc")
        mock_category.save.assert_called_once()
        self.assertEqual(result, mock_category)


if __name__ == "__main__":
    unittest.main()
