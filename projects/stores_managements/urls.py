from django.contrib import admin
from django.urls import path
from .views import StoreCreate,StoreDelete,StoreDetail,StoresList,StoreUpdate

urlpatterns = [
    path('',StoresList.as_view(),name='stores_list'),
    path('store_create',StoreCreate.as_view(),name='store_create'),
    path('store/<int:pk>/',StoreDetail.as_view(),name='store_detail'),
    path('store/<int:pk>/update/',StoreUpdate.as_view(),name='store_update'),
    path('store/<int:pk>/delete/',StoreDelete.as_view(),name='store_delete')
]
