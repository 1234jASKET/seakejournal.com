from django.shortcuts import render, redirect, get_object_or_404
from .models import Dossier
from .forms import DossierForm
from django.http import JsonResponse
from .serializers import dossier_serializer  # <- n'oublie pas cet import


def home(request):
    return render(request, "core/home.html")

def dossier_list(request):
    dossiers = Dossier.objects.all()
    return render(request, "core/list.html", {"dossiers": dossiers})

def dossier_create(request):
    form = DossierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, "core/create.html", {"form": form})

def dossier_update(request, id):
    dossier = get_object_or_404(Dossier, id=id)
    form = DossierForm(request.POST or None, instance=dossier)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, "core/update.html", {"form": form})

def dossier_delete(request, id):
    dossier = get_object_or_404(Dossier, id=id)
    if request.method == "POST":
        dossier.delete()
        return redirect('list')
    
def api_dossiers(request):
    if request.method != "GET":
        return HttpResponseBadRequest("Only GET allowed")
    dossiers = Dossier.objects.all()
    data = [dossier_serializer(d) for d in dossiers]
    return JsonResponse(data, safe=False)    
    return render(request, "core/delete.html", {"dossier": dossier})