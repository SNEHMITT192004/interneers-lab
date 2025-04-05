from products.models import Product, ProductCategory

class ProductService:
    @staticmethod
    def get_all_products():
        return list(Product.objects.all())

    @staticmethod
    def get_product_by_id(product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    @staticmethod
    def create_product(name, description, price,brand):
        product = Product(name=name, description=description, price=price,brand=brand)
        product.save()
        return product

    @staticmethod
    def update_product(product_id, name, description, price):
        product = ProductService.get_product_by_id(product_id)
        if product:
            product.name = name
            product.description = description
            product.price = price
            product.save()
            return product
        return None

    @staticmethod
    def delete_product(product_id):
        product = ProductService.get_product_by_id(product_id)
        if product:
            product.delete()
            return True
        return False

class ProductCategoryService:
    @staticmethod
    def get_all_categories():
        return ProductCategory.objects.all()

    @staticmethod
    def create_category(title, description):
        category = ProductCategory(title=title, description=description)
        category.save()
        return category
