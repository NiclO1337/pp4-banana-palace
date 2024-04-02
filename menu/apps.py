from django.apps import AppConfig


class MenuItemConfig(AppConfig):
    """
    Configuration for the 'menu' application.

    This class defines the metadata for the 'menu' application, including
    the default auto field type for models and the application's name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
