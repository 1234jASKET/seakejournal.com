from django.shortcuts import render
from .models import Ingredient, CoutSupplementaire

# Create your views here.
def calculateur_cogs(request):
    ingredients = Ingredient.objects.all()
    couts_supp = CoutSupplementaire.objects.all()
    
    total_matieres = sum(i.cout_total() for i in ingredients)
    total_supp = sum(c.montant for c in couts_supp)
    cogs_total = total_matieres + total_supp
    quantite_totale = sum(i.kg for i in ingredients)
    cout_par_kg = cogs_total / quantite_totale if quantite_totale else 0

    context = {
        'ingredients': ingredients,
        'couts_supp': couts_supp,
        'total_matieres': total_matieres,
        'cogs_total': cogs_total,
        'cout_par_kg': cout_par_kg,
        'quantite_totale': quantite_totale
    }
    return render(request, 'cogs/calculateur.html', context)