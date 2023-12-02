from django.apps import AppConfig


class DefectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'defects'

    def ready(self):
        import defects.signals
