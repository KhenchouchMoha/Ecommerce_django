from django import forms 
from .models import Store


class StoreForm(forms.ModelForm) : 
    class Meta : 
        model= Store 
        fields= [
            'store_name',
            'store_adresse',
            'store_description',
            'store_numero1',
            'store_numero2',
            'store_email',
            'store_link_linkedin',
            'store_link_instagram',
            'store_link_facebook',
            ]
        widgets = {
           'store_name': forms.TextInput(),
           'store_adresse' : forms.TextInput(),
           'store_description' : forms.TextInput(),
           'store_numero1' : forms.TextInput(),
           'store_numero2' : forms.TextInput(),
           'store_email' : forms.TextInput(),
           'store_link_linkedin' : forms.TextInput(),
           'store_link_instagram' : forms.TextInput(),
           'store_link_facebook' : forms.TextInput(),
        }
