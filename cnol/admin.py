from django.contrib import admin
from .models import Article, Categorie, Publicite

# Register your models here.
# Enregistrement dans l'admin
admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Publicite)
