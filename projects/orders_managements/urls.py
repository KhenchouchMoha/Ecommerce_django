from django.contrib import admin
from django.urls import path
from .views import OrderCreate,OrderUpdate,OrderList,OrderDelete,OrderDetail

urlpatterns = [
    path('',OrderList.as_view(),name='orders_list'),
    path('order_create',OrderCreate.as_view(),name='order_create'),
    path('order/<int:pk>/',OrderDetail.as_view(),name='order_detail'),
    path('order/<int:pk>/update/',OrderUpdate.as_view(),name='order_update'),
    path('order/<int:pk>/delete/',OrderDelete.as_view(),name='order_delete')
]

    
