from django.shortcuts import render
from django.views.generic import ListView, DeleteView,DetailView,CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Products
from .forms import ProductsForm
# Create your views here.

class ProductList(ListView) : 
    model= Products
    template_name='products/product_list.html'
    context_object_name='list_products'


class ProductDetail(DetailView):
    model=Products
    template_name='products/product_detail.html'

class ProductCreate(CreateView) : 
    model= Products
    form_class= ProductsForm
    template_name= 'products/product_form.html'
    success_url=reverse_lazy('product_list')

class ProductUpdate(UpdateView) : 
    model = Products
    form_class=ProductsForm
    template_name='products/update_form.html' 
    success_url=reverse_lazy('product_list')

class ProductDelete(DeleteView) : 
    model = Products
    template_name='products/delete_confirmation.html' 
    success_url=reverse_lazy('product_list')    
