from django.apps import AppConfig


class ReservationConfig(AppConfig):
    """
    Configuration for the 'reservation' application.

    This class defines the metadata for the 'reservation' application, including
    the default auto field type for models and the application's name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservation'
