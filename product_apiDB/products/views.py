# # # products/views.py
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from products.service import ProductService


# # class ProductListView(APIView):
# #     def get(self, request):
# #         products = ProductService.get_all_products()
# #         return Response(products, status=status.HTTP_200_OK)

# #     def post(self, request):
# #         data = request.data
# #         product = ProductService.create_product(data)
# #         return Response(product, status=status.HTTP_201_CREATED)

# # class ProductDetailView(APIView):
# #     def get(self, request, product_id):
# #         product = ProductService.get_product_by_id(product_id)
# #         if product:
# #             return Response(product, status=status.HTTP_200_OK)
# #         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

# #     def put(self, request, product_id):
# #         data = request.data
# #         product = ProductService.update_product(product_id, data)
# #         if product:
# #             return Response(product, status=status.HTTP_200_OK)
# #         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

# #     def delete(self, request, product_id):
# #         success = ProductService.delete_product(product_id)
# #         if success:
# #             return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
# #         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

# # from django.http import HttpResponse

# # def home(request):
# #     return HttpResponse("Welcome to the Product API!")
# # products/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from products.service import ProductService
# from products.models import Product  # Import your Product model if needed
# from products.serializers import ProductSerializer  # Import your serializer if you have one

# class ProductListView(APIView):
#     def get(self, request):
#         product_service = ProductService()  # Create an instance of ProductService
#         products = product_service.get_all_products()  # Call the method on the instance
#         # Assuming you have a serializer to convert products to JSON
#         serializer = ProductSerializer(products, many=True)  # Use a serializer to format the response
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         product_service = ProductService()  # Create an instance of ProductService
#         data = request.data
#         product = product_service.create_product(data['name'], data.get('description'), data['price'])  # Adjust based on your method signature
#         serializer = ProductSerializer(product)  # Use a serializer to format the response
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ProductDetailView(APIView):
#     def get(self, request, product_id):
#         product_service = ProductService()  # Create an instance of ProductService
#         product = product_service.get_product_by_id(product_id)
#         if product:
#             serializer = ProductSerializer(product)  # Use a serializer to format the response
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, product_id):
#         product_service = ProductService()  # Create an instance of ProductService
#         data = request.data
#         product = product_service.update_product(product_id, data['name'], data.get('description'), data['price'])  # Adjust based on your method signature
#         if product:
#             serializer = ProductSerializer(product)  # Use a serializer to format the response
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, product_id):
#         product_service = ProductService()  # Create an instance of ProductService
#         success = product_service.delete_product(product_id)
#         if success:
#             return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Product API!")
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.service import ProductService
from products.serializers import ProductSerializer

class ProductListView(APIView):
    def get(self, request):
        products = ProductService.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        product = ProductService.create_product(data['name'], data.get('description', ""), data['price'])
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Failed to create product"}, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self, request, product_id):
        product = ProductService.get_product_by_id(product_id)
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, product_id):
        data = request.data
        product = ProductService.update_product(product_id, data['name'], data.get('description', ""), data['price'])
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, product_id):
        success = ProductService.delete_product(product_id)
        if success:
            return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Product API!")
