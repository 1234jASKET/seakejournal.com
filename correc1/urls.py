from django.urls import path
from . import views

urlpatterns = [
    path("<int:production_id>/", views.cogs_calculator, name="cogs_calc"),
    
]