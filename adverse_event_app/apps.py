from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "adverse_event_app"
    verbose_name = "Edc Adverse Events Test App"
