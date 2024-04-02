from django.apps import AppConfig


class CustomerConfig(AppConfig):
    """
    Configuration for the 'customer' app.

    This class sets the default auto field to 'django.db.models.BigAutoField'
    and specifies the app name as 'customer'. It also imports signals
    for the 'customer' app when Django starts.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'

    def ready(self):
        """
        Import signals when Django starts.

        This method is called once by Django when the app is ready. It's used
        to import signals for the 'customer' app, ensuring that signal handlers
        are connected.
        """
        import customer.signals