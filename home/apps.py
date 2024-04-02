from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration for the 'home' application.

    This class defines the metadata for the 'home' application, including
    the default auto field type for models and the application's name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
