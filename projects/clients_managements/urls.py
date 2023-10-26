from django.contrib import admin
from django.urls import path,include
from .views import ClientCreate,ClientDelete,ClientList,ClientUpdate,ClientDetail
urlpatterns = [
   path('',ClientList.as_view(),name='clients_list'),
   path('client_create',ClientCreate.as_view(),name='client_create'),
   path('client/<int:pk>/',ClientDetail.as_view(),name='client_detail'),
   path('client/<int:pk>/update/',ClientUpdate.as_view(),name='client_update'),
   path('client/<int:pk>/delete/',ClientDelete.as_view(),name='client_delete'),
]

