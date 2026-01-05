from django.contrib import admin
from .models import Recipe, Ingredient, Production, ProductionIngredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "total_demande_default", "date_created")
    inlines = [IngredientInline]

class ProductionIngredientInline(admin.TabularInline):
    model = ProductionIngredient
    extra = 0
    readonly_fields = ("name","percent","kg","price","cost")

@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ("id","formule_name","total_kg","cogs_total","price_total","date")
    inlines = [ProductionIngredientInline]