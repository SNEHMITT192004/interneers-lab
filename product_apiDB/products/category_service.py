from products.models import ProductCategory, Product

class ProductCategoryService:
    @staticmethod
    def create_category(title, description):
        category = ProductCategory(title=title, description=description)
        category.save()
        return category

    @staticmethod
    def get_all_categories():
        return list(ProductCategory.objects.all())

    @staticmethod
    def get_category_by_id(category_id):
        return ProductCategory.objects.get(id=category_id)

    @staticmethod
    def update_category(category_id, title, description):
        category = ProductCategory.objects.get(id=category_id)
        category.title = title
        category.description = description
        category.save()
        return category

    @staticmethod
    def delete_category(category_id):
        category = ProductCategory.objects.get(id=category_id)
        category.delete()
        return True
