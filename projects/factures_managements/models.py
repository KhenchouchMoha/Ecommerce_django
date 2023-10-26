from django.db import models

# Create your models here.
class Facture(models.Model) : 
    facture_id=models.IntegerField(primary_key=True)
    facture_montant=models.FloatField()
    facture_id_commande=models.IntegerField()
    facture_id_client=models.IntegerField()