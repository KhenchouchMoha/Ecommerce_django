from django import forms 
from .models import Order


class OrderForm(forms.ModelForm) : 
    class Meta : 
        model= Order 
        fields= ['order_username','order_date','order_shipped','order_shippingadresse','order_orderstatus','order_total']
        widgets = {
           'order_username' : forms.TextInput(),
           'order_date' : forms.TextInput(),
           'order_shipped' : forms.TextInput(),
           'order_shippingadresse' : forms.TextInput(),
           'order_orderstatus' : forms.TextInput(),
           'order_total' : forms.TextInput(),
        }


