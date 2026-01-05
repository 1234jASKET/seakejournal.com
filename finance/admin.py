from django.contrib import admin
from .models import Formule, Composant

class ComposantInline(admin.TabularInline):
    model = Composant
    extra = 1
    fields = ("nom", "pourcentage", "prix", "kg", "cout_total")
    readonly_fields = ("kg", "cout_total")

@admin.register(Formule)
class FormuleAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "cout_total",
        "cogs",
        "cout_par_kg",
        "main_oeuvre",
        "transport",
        "autres",
        "profit",
        "projection_mensuelle",
        "projection_annuelle",
    )
    inlines = [ComposantInline]

    # laisser save_model "normal" (ne pas recalculer ici)
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    # appelé APRÈS que les inlines aient été sauvegardés
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        # form.instance est l'objet Formule qui vient d'être sauvegardé
        form.instance.calculer_totaux()

@admin.register(Composant)
class ComposantAdmin(admin.ModelAdmin):
    list_display = ("nom", "pourcentage", "prix", "kg", "cout_total", "formule")
    search_fields = ("nom",)