from django.urls import path
from . import views

urlpatterns = [
    # 🔧 Export Excel
    path(
        "export/excel/<int:production_id>/",
        views.export_production_excel,
        name="export_production_excel"
    ),

    # 🔧 Export PDF
    path(
        "export/pdf/<int:production_id>/",
        views.export_production_pdf,
        name="export_production_pdf"
    ),

    # 🧮 Page COGS (DOIT ÊTRE EN BAS)
    path(
        "<int:production_id>/",
        views.cogs_calculator,
        name="cogs_calc"
    ),
]