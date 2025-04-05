from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Product, ProductCategory


class ProductCategorySerializer(DocumentSerializer):
    class Meta:
        model = ProductCategory
        fields = ['title', 'description']


class ProductSerializer(DocumentSerializer):
    category = ProductCategorySerializer(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'brand', 'category']

    def create(self, validated_data):
        category_data = validated_data.pop("category", None)

        category = None
        if category_data:
            category = ProductCategory.objects(title=category_data["title"]).first()
            if not category:
                category = ProductCategory(**category_data)
                category.save()

        product = Product(**validated_data)
        product.category = category
        product.save()

        # Optional: update category’s products list
        if category and product not in category.products:
            category.products.append(product)
            category.save()

        return product

