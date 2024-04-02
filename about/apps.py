from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration for the 'about' app.

    This class sets the default auto field to 'django.db.models.BigAutoField'
    and specifies the app name as 'about'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
