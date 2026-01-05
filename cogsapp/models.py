from django.db import models

class Recipe(models.Model):
    """Formulation enregistrée / recette"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    total_demande_default = models.FloatField(default=100.0, help_text="Quantité totale par défaut (kg)")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    name = models.CharField(max_length=200)
    percent = models.FloatField(help_text="Pourcentage dans la recette")
    price = models.FloatField(help_text="Prix par kg")

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.name} ({self.percent}%)"


class Production(models.Model):
    formule = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.SET_NULL)
    formule_name = models.CharField(max_length=200, blank=True)
    total_kg = models.FloatField(default=0.0, help_text="Quantité totale de production prévue (kg)")
    batch = models.CharField(max_length=50, blank=True)
    line = models.CharField(max_length=50, blank=True)
    operator = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # Gestion des quantités réelles
    kg_acheter = models.FloatField(default=0.0, help_text="Kg achetés pour la production")
    kg_presse = models.FloatField(default=0.0, help_text="Kg envoyés à la presse")
    kg_retour = models.FloatField(default=0.0, help_text="Kg retournés après production")

    # Coûts variables et fixes
    total_materials = models.FloatField(default=0.0)
    labor_cost = models.FloatField(default=0.0)
    energy_cost = models.FloatField(default=0.0)
    packaging_cost = models.FloatField(default=0.0)
    overhead_percent = models.FloatField(default=0.0, help_text="Pourcentage des frais généraux")
    overhead_cost = models.FloatField(default=0.0)
    cogs_total = models.FloatField(default=0.0)
    cost_per_kg = models.FloatField(default=0.0)

    # Prix de vente et marge
    margin_percent = models.FloatField(default=0.0)
    price_per_kg = models.FloatField(default=0.0)
    price_total = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.formule_name or 'Production'} — {self.batch or self.date.strftime('%Y%m%d%H%M')}"


class ProductionIngredient(models.Model):
    production = models.ForeignKey(Production, on_delete=models.CASCADE, related_name="production_ingredients")
    name = models.CharField(max_length=200)
    percent = models.FloatField()
    kg = models.FloatField()
    price = models.FloatField()
    cost = models.FloatField()

    def __str__(self):
        return f"{self.name} — Production {self.production.id}"