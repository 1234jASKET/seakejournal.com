from django.apps import AppConfig


class FinanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finance'

    def ready(self):
        # importer les signaux ici pour éviter les imports au niveau module
        import finance.signals  # noqa: F401