from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, UpdateView,DetailView,CreateView
from .models import Store
from .forms import StoreForm
from django.urls import reverse_lazy


class StoresList(ListView) : 
    model = Store 
    template_name='stores/store_list.html'
    context_object_name='stores_list'

class StoreDetail(DetailView) :
    model = Store 
    template_name='stores/store_detail.html'

class StoreCreate(CreateView) :
    model =Store
    form_class= StoreForm
    template_name='stores/stores_forms.html'
    success_url=reverse_lazy('stores_list')

class StoreUpdate(UpdateView) : 
    model=Store
    form_class=StoreForm
    template_name='stores/stores_forms.html'
    success_url=reverse_lazy('stores_list')

class StoreDelete(DeleteView) : 
    model =Store 
    template_name='stores/confirmation_delete_store.html'
    success_url=reverse_lazy('stores_list')    




