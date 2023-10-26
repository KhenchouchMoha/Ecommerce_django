from django import forms
from .models import Client
class ClientForm(forms.ModelForm) :
   class Meta  : 
      model =Client
      fields= [
            'client_firstName',
            'client_SecondName',
            'client_Adresse',
            'client_Number',
            'client_Email',
            'client_login',
            ]
      widgets = {
           'client_firstName': forms.TextInput(),
           'client_SecondName': forms.TextInput(),
           'client_Adresse' : forms.TextInput(),
           'Client_Number' : forms.TextInput(),
           'client_Email' : forms.TextInput(),
           'client_login' : forms.TextInput(),
           'client_mot_de_passe' : forms.TextInput(),
           'client_login' :  forms.TextInput(),
      }
