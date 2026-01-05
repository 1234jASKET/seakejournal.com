from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # CRUD
    path('dossiers/', views.dossier_list, name='list'),
    path('dossiers/create/', views.dossier_create, name='create'),
    path('dossiers/update/<int:id>/', views.dossier_update, name='update'),
    path('dossiers/delete/<int:id>/', views.dossier_delete, name='delete'),

    # API
    path('api/dossiers/', views.api_dossiers, name='api_dossiers'),
]