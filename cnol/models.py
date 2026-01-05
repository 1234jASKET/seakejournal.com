from django.db import models

# Create your models here.
# Catégories d'articles
class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

# Articles CNOL
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True, blank=True)
    publie = models.BooleanField(default=False)

    def __str__(self):
        return self.titre

# Publicités CNOL
class Publicite(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()

    def __str__(self):
        return self.titre
