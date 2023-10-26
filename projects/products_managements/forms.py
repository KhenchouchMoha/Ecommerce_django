from django import forms 
from .models import Products


class ProductsForm(forms.ModelForm) : 
    class Meta : 
        model= Products 
        fields= ['product_title','product_descriptions','product_price','product_discount','product_in_stock','product_categories' ]
        widgets = {
           'product_title': forms.TextInput(),
           'product_descriptions' : forms.Textarea(),
           'product_price' : forms.TextInput(),
           'product_discount' : forms.TextInput(),
           'product_in_stock' : forms.TextInput(),
        #   'images': forms.FileInput(),
           'product_categories': forms.Select(),
        }



