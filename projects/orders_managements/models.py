from django.db import models

# Create your models here.
class Order(models.Model) : 
    order_id = models.IntegerField(primary_key=True)
    order_username=models.CharField(max_length=50)
    order_date=models.DateTimeField()
    order_shipped=models.DateTimeField()
    order_shippingadresse=models.CharField(max_length=50)
    order_orderstatus=models.BooleanField()
    order_total=models.FloatField()