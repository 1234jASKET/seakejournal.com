from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from .models import Formule
from .forms import FormuleForm


# -------------------------------
# CRUD FORMULES (SANS HTML)
# -------------------------------

# Liste des formules (FORMAT JSON)
def formule_list(request):
    data = list(Formule.objects.values())
    return JsonResponse({"formules": data})


# Créer une formule
def formule_create(request):
    if request.method == "POST":
        form = FormuleForm(request.POST)
        if form.is_valid():
            formule = form.save()
            return JsonResponse({"status": "ok", "id": formule.id})
        return JsonResponse({"status": "error", "errors": form.errors})
    
    return JsonResponse({"error": "POST required"})


# Modifier une formule
def formule_update(request, id):
    formule = get_object_or_404(Formule, id=id)

    if request.method == "POST":
        form = FormuleForm(request.POST, instance=formule)
        if form.is_valid():
            formule = form.save()
            return JsonResponse({"status": "ok", "id": formule.id})
        return JsonResponse({"status": "error", "errors": form.errors})

    return JsonResponse({"error": "POST required"})


# Supprimer une formule
def formule_delete(request, id):
    formule = get_object_or_404(Formule, id=id)

    if request.method == "POST":
        formule.delete()
        return JsonResponse({"status": "deleted"})

    return JsonResponse({"error": "POST required"})


# -------------------------------
# COGS CALCULATOR (SANS HTML)
# -------------------------------

def cogs_calculator(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"})

    try:
        total_demande = float(request.POST.get("total_demande"))
        noms = request.POST.getlist("nom")
        pourcentages = request.POST.getlist("pourcentage")
        prix = request.POST.getlist("prix")

        from .utils import calculer_cogs
        result = calculer_cogs(total_demande, noms, pourcentages, prix)

        return JsonResponse({"result": result})

    except Exception as e:
        return JsonResponse({"error": str(e)})