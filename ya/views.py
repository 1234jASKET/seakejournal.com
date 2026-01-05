import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from django.shortcuts import render
from django.utils import timezone
from django.conf import settings

from .models import Cout


def couts(request):
    if request.method == "POST":
        Cout.objects.all().delete()

        noms = request.POST.getlist("nom")
        quantites = request.POST.getlist("quantite")
        prixs = request.POST.getlist("prix_unitaire")

        for nom, qte, prix in zip(noms, quantites, prixs):
            if not nom.strip():
                continue
            try:
                qte = float(str(qte).replace(",", "."))
                prix = float(str(prix).replace(",", "."))
            except ValueError:
                continue

            Cout.objects.create(
                nom=nom,
                quantite=qte,
                prix_unitaire=prix,
                total=qte * prix,
                date_creation=timezone.now()
            )

    couts_list = Cout.objects.all()
    return render(request, "ya/couts.html", {"couts": couts_list})


def graphique(request):
    couts_list = Cout.objects.all()
    if not couts_list.exists():
        return render(request, "ya/graphique.html", {"message": "Aucune donnée à afficher"})

    noms = [c.nom for c in couts_list]
    totaux = [c.total for c in couts_list]

    plt.figure(figsize=(8, 4))
    plt.bar(noms, totaux)
    plt.title("Coûts par ingrédient")
    plt.ylabel("Coût total ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    path = os.path.join(settings.BASE_DIR, "ya", "static", "ya", "graphique.png")
    os.makedirs(os.path.dirname(path), exist_ok=True)  # ← créer le dossier si nécessaire
    plt.savefig(path)
    plt.close()

    return render(request, "ya/graphique.html", {"image_path": "ya/graphique.png"})