from django import forms
from .models import Formule

class FormuleForm(forms.ModelForm):
    class Meta:
        model = Formule
        fields = [
            "nom",
            "description",
            "total_demande",
            "prix_unitaire",
            "cout_total",
            "cogs",
            "cout_par_kg",
            "profit",
            "projection_mensuelle",
            "projection_annuelle",
            "main_oeuvre",
            "transport",
            "autres",
        ]