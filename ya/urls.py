from django.urls import path
from . import views

urlpatterns = [
    path('couts/', views.couts, name='couts'),
    path('graphique/', views.graphique, name='graphique'),
]