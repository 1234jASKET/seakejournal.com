from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=100)

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    publie = models.BooleanField(default=False)

class Publicite(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
