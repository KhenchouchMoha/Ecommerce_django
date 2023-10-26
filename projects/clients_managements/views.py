from django.shortcuts import render
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from .models import Client
from .forms import ClientForm
from django.urls import reverse_lazy
# Create your views here.

class ClientList(ListView) :
    model= Client 
    template_name ='clients/clients_list.html'
    context_object_name='clients_list'

class ClientDetail(DetailView) : 
    model = Client 
    template_name='clients/client_detail.html'

class ClientCreate(CreateView) : 
    model =Client 
    form_class = ClientForm
    template_name='clients/clients_forms.html'
    success_url=reverse_lazy('clients_list')

class ClientUpdate(UpdateView):
    model = Client
    form_class=ClientForm
    template_name='clients/clients_forms.html'
    success_url=reverse_lazy('clients_list')

class ClientDelete(DeleteView) : 
    model = Client 
    template_name = 'clients/confirmation_delete_client.html'
    success_url = reverse_lazy('clients_list')
