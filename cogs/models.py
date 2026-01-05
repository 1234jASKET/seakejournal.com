from django.db import models

# Create your models here.
class Ingredient(models.Model):
    nom = models.CharField(max_length=50)
    kg = models.FloatField()
    prix_par_kg = models.FloatField()

    def cout_total(self):
        return self.kg * self.prix_par_kg

    def pourcentage(self):
        total_kg = sum(i.kg for i in Ingredient.objects.all())
        if total_kg == 0:
            return 0
        return (self.kg / total_kg) * 100

class CoutSupplementaire(models.Model):
    nom = models.CharField(max_length=50)
    montant = models.FloatField()