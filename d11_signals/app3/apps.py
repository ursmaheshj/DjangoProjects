from django.apps import AppConfig


class App3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app3'

    # def ready(self) -> None:
    #     import app3.signals

