from django.db import models


CATEGORIES_CHOICES= (
    ('IM','informatique et Multimedia'),
    ('V','Vehicules'),
    ('I','Immobilier'),
    ('MB','Maison et bureau'),
    ('BB','Beaute et bienetre'),
    ('L','Loisirs'),
)
# Create your models here.
class Products(models.Model) : 
    product_id=models.IntegerField(primary_key=True)
    product_title=models.CharField(max_length=500)
    product_descriptions=models.TextField()
    product_price=models.FloatField()
    product_discount=models.IntegerField()
    product_in_stock=models.IntegerField()
    product_quantite=models.IntegerField()
    product_categories=models.CharField(choices=CATEGORIES_CHOICES,max_length=26)
    