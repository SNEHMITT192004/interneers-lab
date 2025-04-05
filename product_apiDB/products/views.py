# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from products.service import ProductService
# from products.serializers import ProductSerializer
# from products.serializers import ProductCategorySerializer


# class ProductListView(APIView):
#     def get(self, request):
#         products = ProductService.get_all_products()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         data = request.data
#         name = data.get('name')
#         description = data.get('description', "")
#         price = data.get('price')
#         brand = data.get('brand')

#         if not all([name, price, brand]):
#             return Response(
#                 {"error": "Missing required fields: name, price, brand"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         product = ProductService.create_product(name, description, price, brand)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



# class ProductDetailView(APIView):
#     def get(self, request, product_id):
#         product = ProductService.get_product_by_id(product_id)
#         if product:
#             serializer = ProductSerializer(product)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, product_id):
#         data = request.data
#         product = ProductService.update_product(product_id, data['name'], data.get('description', ""), data['price'])
#         if product:
#             serializer = ProductSerializer(product)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, product_id):
#         success = ProductService.delete_product(product_id)
#         if success:
#             return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#         return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def get(self, request, product_id):
        product = self.get_object(product_id)
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ProductCategoryView(APIView):
    def get(self, request):
        from .service import ProductCategoryService
        categories = ProductCategoryService.get_all_categories()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        from .service import ProductCategoryService
        data = request.data
        category = ProductCategoryService.create_category(data['title'], data['description'])
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data, status=201)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Product, ProductCategory
from products.serializers import ProductSerializer

# class ProductsByCategoryView(APIView):
#     def get(self, request, category_id):
#         try:
#             category = ProductCategory.objects.get(id=category_id)
#         except ProductCategory.DoesNotExist:
#             return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

#         products = Product.objects(category=category)
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class ProductsByCategoryView(APIView):
    def get(self, request, title):
        try:
            category = ProductCategory.objects.get(title=title)
        except ProductCategory.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
#6. Add APIs to add/remove products from category
# class ModifyCategoryProductsView(APIView):
#     def post(self, request, category_id):
#         product_id = request.data['product_id']
#         category = ProductCategory.objects.get(id=category_id)
#         product = Product.objects.get(id=product_id)
#         category.products.append(product)
#         product.category = category
#         category.save()
#         product.save()
#         return Response({"message": "Product added to category"})

#     def delete(self, request, category_id):
#         product_id = request.data['product_id']
#         category = ProductCategory.objects.get(id=category_id)
#         product = Product.objects.get(id=product_id)
#         category.products.remove(product)
#         product.category = None
#         category.save()
#         product.save()
#         return Response({"message": "Product removed from category"})

class ModifyCategoryProductsView(APIView):
    def post(self, request, title, action):
        product_id = request.data.get('product_id')

        try:
            category = ProductCategory.objects.get(title=title)
            product = Product.objects.get(id=product_id)
        except (ProductCategory.DoesNotExist, Product.DoesNotExist):
            return Response({"error": "Invalid category title or product ID"}, status=status.HTTP_404_NOT_FOUND)

        if action == 'add_product':
            if product not in category.products:
                category.products.append(product)
                product.category = category
                category.save()
                product.save()
                return Response({"message": "Product added to category"}, status=status.HTTP_200_OK)
            return Response({"message": "Product already in category"}, status=status.HTTP_200_OK)

        elif action == 'remove_product':
            if product in category.products:
                category.products.remove(product)
                product.category = None
                category.save()
                product.save()
                return Response({"message": "Product removed from category"}, status=status.HTTP_200_OK)
            return Response({"message": "Product not in category"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)


from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Product API!")

