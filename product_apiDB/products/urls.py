# products/urls.py
from django.urls import path
from .views import ProductListView, ProductDetailView, home  # Import the home view

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),  # For `/products/`
    path('<int:product_id>/', ProductDetailView.as_view(), name='product-detail'),  # For `/products/1/`
    path('home/', home, name='home'),  # Optional: For `/products/home/`
]