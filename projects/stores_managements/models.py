from django.db import models
from django import forms
# Create your models here.
class Store(models.Model) : 
    store_id=models.IntegerField(primary_key=True)
    store_name=models.CharField(max_length=50)
    store_adresse=models.CharField(max_length=50)
    store_description=models.TextField(default='Write your description')
    store_numero1=models.TextField(default='Write your number')
    store_numero2=models.TextField(default='Write your number')
    store_email=models.EmailField(default='example@gmail.com')
    store_link_linkedin=models.CharField(max_length=500,default='Link facebook')
    store_link_instagram=models.CharField(max_length=500,default='Link facebook')
    store_link_facebook=models.CharField(max_length=500,default='Link facebook')
    store_incomes=models.FloatField()
