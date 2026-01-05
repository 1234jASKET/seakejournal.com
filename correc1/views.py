from django.shortcuts import render, redirect, get_object_or_404
from .models import Production, ProductionIngredient
from .forms import ProductionIngredientForm


def cogs_calculator(request, production_id):
    production = get_object_or_404(Production, id=production_id)

    if request.method == "POST":

        # --- 1) AJOUT D’INGRÉDIENT ---
        if 'name' in request.POST:  # formulaire ingrédient
            form = ProductionIngredientForm(request.POST)
            if form.is_valid():
                ing = form.save(commit=False)
                ing.production = production
                # inutile de recalculer si c'est déjà dans save()
                # ing.cost = (ing.kg or 0) * (ing.price or 0)
                ing.save()

                production.calculate_totals()
                production.save()

                return redirect("cogs_calc", production_id=production.id)

        # --- 2) CALCUL PRINCIPAL COGS ---
        def get_float(name):
            value = request.POST.get(name, "0").replace(",", ".")
            try:
                return float(value)
            except ValueError:
                return 0

        production.total_kg = get_float("total_kg")
        production.quantity_sent = get_float("quantity_sent")
        production.quantity_returned = get_float("quantity_returned")
        production.sale_price_per_kg = get_float("sale_price_per_kg")

        production.labor_cost = get_float("labor_cost")
        production.energy_cost = get_float("energy_cost")
        production.packaging_cost = get_float("packaging_cost")
        production.overhead_cost = get_float("overhead_cost")

        production.calculate_totals()
        production.save()

        return redirect("cogs_calc", production_id=production.id)

    # --- GET Request ---
    ingredients = ProductionIngredient.objects.filter(production=production)
    form = ProductionIngredientForm()

    return render(request, "correc1/cogs_calculator.html", {
        "production": production,
        "ingredients": ingredients,
        "form": form,
    })
