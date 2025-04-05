"""
URL configuration for product_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# product_api/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from products.views import home  # Import the home view

# urlpatterns = [
#     path('', home, name='home'),  # This will match the root URL
#     path('admin/', admin.site.urls),
#     path('products/', include('products.urls')),  # Ensure this line is correct
#     # path('categories/', include('categories.urls')),   # Category-related endpoints 🔥
# ]

# from django.urls import path
# from products.views import ProductListView, ProductDetailView, home

# urlpatterns = [
#     path('', home, name='home'),
#     path('products/', ProductListView.as_view(), name='product-list'),
#     path('products/<str:product_id>/', ProductDetailView.as_view(), name='product-detail'),  # ✅ Change int to str
#     path('products/home/', home, name='home'),
# ]

# from django.urls import path
# from products.views import (
#     ProductListView,
#     ProductDetailView,
#     ProductCategoryView,
#     ProductsByCategoryView,
#     ModifyCategoryProductsView,
#     home,
# )

# urlpatterns = [
#     path('', home, name='home'),
    
#     # Categories first (more specific URLs before dynamic ones)
#     path('products/categories/<str:category_id>/products/modify/', ModifyCategoryProductsView.as_view(), name='modify-category-products'),
#     path('products/categories/<str:category_id>/products/', ProductsByCategoryView.as_view(), name='products-by-category'),
#     path('products/categories/', ProductCategoryView.as_view(), name='product-category'),

#     # Product routes
#     path('products/', ProductListView.as_view(), name='product-list'),
#     path('products/<str:product_id>/', ProductDetailView.as_view(), name='product-detail'),

#     path('products/home/', home, name='home'),
# ]

from django.urls import path
from products.views import (
    ProductListView,
    ProductDetailView,
    ProductCategoryView,
    ProductsByCategoryView,
    ModifyCategoryProductsView,
    home,
)

urlpatterns = [
    path('', home, name='home'),

    # Category-related views using category title
    path('products/categories/<str:title>/products/', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('products/categories/<str:title>/<str:action>/', ModifyCategoryProductsView.as_view(), name='modify-category-products'),
    path('products/categories/', ProductCategoryView.as_view(), name='product-category'),

    # Product-related views
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<str:product_id>/', ProductDetailView.as_view(), name='product-detail'),

    path('products/home/', home, name='home'),
]
