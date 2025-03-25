from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import ProductSerializer

# In-memory storage (list of product dictionaries)
products_db = []
product_id_counter = 1  # To track unique IDs

# class ProductViewSet(viewsets.ViewSet):
#     # GET /products/ - List all products
#     def list(self, request):
#         return Response(products_db, status=status.HTTP_200_OK)

#     # POST /products/ - Create a new product
#     def create(self, request):
#         global product_id_counter
#         data = request.data
#         data['id'] = product_id_counter
#         product_id_counter += 1
#         products_db.append(data)
#         return Response(data, status=status.HTTP_201_CREATED)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        """ Override create method to return full product details after creation """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    # GET /products/{id}/ - Retrieve a product by ID
    def retrieve(self, request, pk=None):
        product = next((p for p in products_db if p["id"] == int(pk)), None)
        if product:
            return Response(product, status=status.HTTP_200_OK)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    # PUT /products/{id}/ - Update a product by ID
    def update(self, request, pk=None):
        product = next((p for p in products_db if p["id"] == int(pk)), None)
        if product:
            product.update(request.data)
            return Response(product, status=status.HTTP_200_OK)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    # DELETE /products/{id}/ - Delete a product by ID
    def destroy(self, request, pk=None):
        global products_db
        products_db = [p for p in products_db if p["id"] != int(pk)]
        return Response({"message": "Product deleted"}, status=status.HTTP_204_NO_CONTENT)

