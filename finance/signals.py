from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Composant, Formule

def calculer_formule(formule):
    composants = formule.composants.all()
    total_kg = formule.total_demande

    cout_total = 0.0

    for c in composants:
        # Calcul kg proportionnel à total_demande
        kg = round((c.pourcentage / 100) * total_kg, 3)
        cout_c = round(kg * c.prix, 2)
        cout_total += cout_c

        # Update composant sans trigger post_save
        Composant.objects.filter(id=c.id).update(kg=kg, cout_total=cout_c)

    # Update formule
    Formule.objects.filter(id=formule.id).update(
        cout_total=round(cout_total, 2),
        cogs=round(cout_total, 2),
        cout_par_kg=round(cout_total / total_kg, 2)
    )

@receiver(post_save, sender=Composant)
@receiver(post_delete, sender=Composant)
def maj_formule(sender, instance, **kwargs):
    calculer_formule(instance.formule)