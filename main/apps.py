from django.apps import AppConfig
from django.dispatch import Signal


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Практик.ru'


# isinstance
user_registered = Signal()

