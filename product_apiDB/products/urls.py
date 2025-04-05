# # products/urls.py
# from django.urls import path
# from .views import ProductListView, ProductDetailView, home  # Import the home view
# from products.views import (
#     ProductCategoryListCreateView,
#     ProductsByCategoryView,
#     AddProductToCategoryView,
#     RemoveProductFromCategoryView
# )


# urlpatterns = [
#     path('', ProductListView.as_view(), name='product-list'),  # For `/products/`
#     path('<int:product_id>/', ProductDetailView.as_view(), name='product-detail'),  # For `/products/1/`
#     path('home/', home, name='home'),  # Optional: For `/products/home/`
#     # path('categories/<str:category_id>/products/', ProductsByCategoryView.as_view(), name='products-by-category'),
#     path('', ProductCategoryListCreateView.as_view(), name='category-list-create'),
#     path('<str:category_id>/products/', ProductsByCategoryView.as_view(), name='products-by-category'),
#     path('<str:category_id>/add_product/', AddProductToCategoryView.as_view(), name='add-product-to-category'),
#     path('<str:category_id>/remove_product/', RemoveProductFromCategoryView.as_view(), name='remove-product-from-category'),
# ]
# products/urls.py

from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCategoryView,
    ProductsByCategoryView,
    ModifyCategoryProductsView,
    home,
)

urlpatterns = [
    # more specific routes first
    path('categories/<str:title>/<str:action>/', ModifyCategoryProductsView.as_view()),

    path('categories/<str:title>/products/', ProductsByCategoryView.as_view()),
    path('categories/', ProductCategoryView.as_view()),

    # product routes
    path('', ProductListView.as_view()),
    path('<str:product_id>/', ProductDetailView.as_view()),

    path('home/', home, name='home'),
]

