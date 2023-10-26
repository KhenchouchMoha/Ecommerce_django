from django.contrib import admin
from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate,ProductDelete,ProductUpdate
urlpatterns = [
    path('',ProductList.as_view(),name='product_list'),
    path('product/<int:pk>/',ProductDetail.as_view(),name='product_detail'),
    path('add_new_product/',ProductCreate.as_view(),name='product_create'),
    path('product/<int:pk>/delete',ProductDelete.as_view(),name='product_delete'),
    path('product/<int:pk>/update',ProductUpdate.as_view(),name='product_update'),
]
