from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.products_view, name='index'),
    path('products/', views.products_view, name='products_view'),
    path('products/add/', views.add_product, name='add_product'),
    path('categories/add', views.category_add_view, name='category_add_view'),
    path('products/<int:pk>', views.product_view, name='product_view'),
]