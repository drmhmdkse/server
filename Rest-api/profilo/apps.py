from django.apps import AppConfig


class ProfiloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profilo'

    def ready(self):
        import profilo.signals
