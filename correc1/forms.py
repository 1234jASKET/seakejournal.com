from django import forms
from .models import ProductionIngredient

class ProductionIngredientForm(forms.ModelForm):
    class Meta:
        model = ProductionIngredient
        fields = ['name', 'kg', 'price']
        labels = {
            'name': 'Nom',
            'kg': 'Quantité (kg)',
            'price': 'Prix/kg',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }