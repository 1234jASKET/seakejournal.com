from django.db import models

class Cout(models.Model):
    nom = models.CharField(max_length=50)
    quantite = models.FloatField()
    prix_unitaire = models.FloatField()
    total = models.FloatField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom