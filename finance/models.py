from django.db import models

class Formule(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # Paramètres d'entrée
    total_demande = models.FloatField(default=100.0)  # Quantité totale demandée (kg)
    prix_unitaire = models.FloatField(default=0.0)    # Prix de vente par kg

    # Calcul automatique
    cout_total = models.FloatField(default=0.0)
    cogs = models.FloatField(default=0.0)
    cout_par_kg = models.FloatField(default=0.0)

    # Coûts fixes
    main_oeuvre = models.FloatField(default=0.0)
    transport = models.FloatField(default=0.0)
    autres = models.FloatField(default=0.0)

    # Résultats calculés
    profit = models.FloatField(default=0.0)
    projection_mensuelle = models.FloatField(default=0.0)
    projection_annuelle = models.FloatField(default=0.0)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    def calculer_totaux(self):
        # Calcul du COGS total depuis les composants
        self.cogs = sum(c.cout_total for c in self.composants.all())
        self.cout_total = self.cogs
        self.cout_par_kg = self.cogs / self.total_demande if self.total_demande else 0

        # Dépenses totales
        depenses_totales = self.cogs + self.main_oeuvre + self.transport + self.autres

        # Profit et projections
        revenu_total = self.total_demande * self.prix_unitaire
        self.profit = revenu_total - depenses_totales
        self.projection_mensuelle = self.profit
        self.projection_annuelle = self.projection_mensuelle * 12

        # Sauvegarde
        self.save(update_fields=[
            "cout_total",
            "cogs",
            "cout_par_kg",
            "profit",
            "projection_mensuelle",
            "projection_annuelle"
        ])


class Composant(models.Model):
    formule = models.ForeignKey(
        Formule,
        on_delete=models.CASCADE,
        related_name="composants"
    )
    nom = models.CharField(max_length=200)
    pourcentage = models.FloatField(help_text="Pourcentage (%) du mélange")
    prix = models.FloatField(help_text="Prix par kg")
    
    # Calcul automatique
    kg = models.FloatField(default=0.0)
    cout_total = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        # Calcul automatique à partir du pourcentage
        self.kg = self.formule.total_demande * (self.pourcentage / 100)
        self.cout_total = self.kg * self.prix
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} ({self.pourcentage}%)"