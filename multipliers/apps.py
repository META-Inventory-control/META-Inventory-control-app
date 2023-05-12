from django.apps import AppConfig


class MultipliersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "multipliers"

    def ready(self):
        import multipliers.signals
