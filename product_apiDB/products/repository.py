from products.models import Product

class ProductRepository:
    def create_product(self, name, description, price):
        product = Product(name=name, description=description, price=price)
        product.save()
        return product

    def get_all_products(self):
        return Product.objects()

    def get_product_by_id(self, product_id):
        return Product.objects.get(id=product_id)

    def update_product(self, product_id, name, description, price):
        product = self.get_product_by_id(product_id)
        product.update(name=name, description=description, price=price)
        return product.reload()

    def delete_product(self, product_id):
        product = self.get_product_by_id(product_id)
        product.delete()