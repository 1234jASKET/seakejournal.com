from django.urls import path
from . import views

urlpatterns = [
    path('', views.formule_list, name='finance_list'),
    path('create/', views.formule_create, name='finance_create'),
    path('update/<int:id>/', views.formule_update, name='finance_update'),
    path('delete/<int:id>/', views.formule_delete, name='finance_delete'),

    # Calcul COGS
    path('cogs/', views.cogs_calculator, name='finance_cogs'),
]