from django.db import models


class Production(models.Model):
    formule_name = models.CharField(max_length=200)

    # Champs pour calculs
    total_kg = models.FloatField(default=0)
    quantity_sent = models.FloatField(default=0)
    quantity_returned = models.FloatField(default=0)
    sale_price_per_kg = models.FloatField(default=0)

    # Coûts divers
    labor_cost = models.FloatField(default=0)
    energy_cost = models.FloatField(default=0)
    packaging_cost = models.FloatField(default=0)
    overhead_cost = models.FloatField(default=0)

    # Totaux
    total_materials = models.FloatField(default=0)
    cogs_total = models.FloatField(default=0)
    cost_per_kg = models.FloatField(default=0)
    revenue = models.FloatField(default=0)
    profit = models.FloatField(default=0)

    def calculate_totals(self):
        # Total matières (somme des ingrédients liés)
        self.total_materials = sum(
            i.kg * i.price for i in self.ingredients.all()
        )

        # COGS = matières + frais
        self.cogs_total = (
            self.total_materials +
            self.labor_cost +
            self.energy_cost +
            self.packaging_cost +
            self.overhead_cost
        )

        # Coût par kg
        if self.total_kg > 0:
            self.cost_per_kg = self.cogs_total / self.total_kg
        else:
            self.cost_per_kg = 0

        # Revenu
        self.revenue = self.quantity_sent * self.sale_price_per_kg

        # Profit
        self.profit = self.revenue - self.cogs_total

    def __str__(self):
        return self.formule_name


class ProductionIngredient(models.Model):
    production = models.ForeignKey(
        Production,
        related_name="ingredients",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    kg = models.FloatField(default=0)
    price = models.FloatField(default=0)
    cost = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        # Calcul automatique du coût
        self.cost = (self.kg or 0) * (self.price or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.kg} kg)"
