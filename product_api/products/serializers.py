from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    quantity = serializers.IntegerField(min_value=0)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'brand', 'quantity', 'created_at', 'updated_at']
