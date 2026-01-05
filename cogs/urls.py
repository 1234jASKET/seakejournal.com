from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculateur_cogs, name='calculateur_cogs'),
]