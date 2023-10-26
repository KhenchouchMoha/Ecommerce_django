from django.db import models

# Create your models here.
class Client(models.Model) : 
    client_id = models.IntegerField(primary_key=True)
    client_firstName=models.CharField(max_length=50)
    client_SecondName=models.CharField(max_length=50)
    client_Adresse=models.TextField(default='adresse')
    client_Number=models.TextField(default='060000000')
    client_Email=models.EmailField(default='example@gmail.com')
    client_login=models.CharField(max_length=50)
    client_mot_de_passe=models.CharField(max_length=50)