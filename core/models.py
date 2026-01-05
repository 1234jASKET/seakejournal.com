from django.db import models

# Create your models here.
class Dossier(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
