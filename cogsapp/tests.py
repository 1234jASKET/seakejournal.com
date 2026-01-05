from django import forms
from .models import ProductionIngredient

class ProductionIngredientForm(forms.ModelForm):
    class Meta:
        model = ProductionIngredient
        fields = ['name', 'percent', 'kg', 'price']