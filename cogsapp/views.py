from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductionIngredientForm
from .models import Production, ProductionIngredient

def cogs_calculator(request, production_id):
    production = get_object_or_404(Production, id=production_id)

    if request.method == "POST":
        form = ProductionIngredientForm(request.POST)
        if form.is_valid():
            new_ing = form.save(commit=False)
            new_ing.production = production
            new_ing.cost = new_ing.kg * new_ing.price
            new_ing.save()

            # Recalcul des ingrédients
            ingredients = ProductionIngredient.objects.filter(production=production)

            # Total matières (somme des coûts)
            production.total_materials = sum(i.cost for i in ingredients)

            # Sécuriser les champs optionnels (pour éviter les erreurs)
            labor = getattr(production, "labor_cost", 0) or 0
            energy = getattr(production, "energy_cost", 0) or 0
            packaging = getattr(production, "packaging_cost", 0) or 0
            overhead = getattr(production, "overhead_cost", 0) or 0
            total_kg = getattr(production, "total_kg", 0) or 0

            # COGS complet
            production.cogs_total = (
                production.total_materials +
                labor + energy + packaging + overhead
            )

            # Coût par kg (sécurisé)
            if total_kg > 0:
                production.cost_per_kg = production.cogs_total / total_kg

            production.save()

            return redirect('cogs_calc', production_id=production.id)

    else:
        form = ProductionIngredientForm()

    ingredients = ProductionIngredient.objects.filter(production=production)

    return render(request, "cogs_calculator.html", {
        'production': production,
        'ingredients': ingredients,
        'form': form,
    })


# EXPORT EXCEL
def export_production_excel(request, production_id):
    from openpyxl import Workbook
    from django.http import HttpResponse

    production = Production.objects.get(id=production_id)
    ingredients = ProductionIngredient.objects.filter(production=production)

    wb = Workbook()
    ws = wb.active
    ws.title = "COGS Export"

    ws.append(["Name", "KG", "Price", "Cost"])

    for ing in ingredients:
        ws.append([ing.name, ing.kg, ing.price, ing.cost])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    filename = f"production_{production_id}.xlsx"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    wb.save(response)

    return response


# EXPORT PDF
def export_production_pdf(request, production_id):
    from reportlab.pdfgen import canvas
    from django.http import HttpResponse

    production = Production.objects.get(id=production_id)
    ingredients = ProductionIngredient.objects.filter(production=production)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="production_{production_id}.pdf"'

    p = canvas.Canvas(response)
    y = 800

    p.drawString(100, y, f"Production ID: {production_id}")
    y -= 40

    for ing in ingredients:
        p.drawString(100, y, f"{ing.name} — {ing.kg} kg — {ing.price}$/kg — Cost: {ing.cost}$")
        y -= 20

    p.showPage()
    p.save()

    return response