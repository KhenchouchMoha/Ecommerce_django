from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView,ListView
from .models import Order
from django.urls import reverse_lazy
from .forms import OrderForm

class OrderList(ListView) : 
    model=Order
    template_name='orders/orders_list.html'
    context_object_name='orders_list'


class OrderCreate(CreateView) : 
    model = Order 
    form_class=OrderForm
    template_name='orders/order_form.html'
    success_url=reverse_lazy('orders_list')


class OrderDetail(DetailView):
    model=Order 
    template_name='orders/order_detail.html'

class OrderUpdate(UpdateView) : 
    model=Order
    form_class=OrderForm
    template_name='orders/order_form.html'
    success_url=reverse_lazy('orders_list')

class OrderDelete(DeleteView) : 
    model=Order
    template_name='orders/order_delete_confirmation.html'
    success_url=reverse_lazy('orders_list')


