from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Customer


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kvargs):
    """
    Create a Customer instance for a new User.

    This signal handler is connected to the post_save signal of the User model.
    It creates a Customer instance for a new User instance.

    **Parameters:**
    - `sender`: The model class that sent the signal.
    - `instance`: The instance of the model that triggered the signal.
    - `created`: A boolean indicating whether a new record was created.
    - `**kwargs`: Additional keyword arguments.
    """
    if created:
        Customer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_customer(sender, instance, **kvargs):
    """
    Save the Customer instance associated with a User.

    This signal handler is connected to the post_save signal of the User model.
    It ensures that the Customer instance associated with a User is saved whenever
    the User instance is saved.

    **Parameters:**
    - `sender`: The model class that sent the signal.
    - `instance`: The instance of the model that triggered the signal.
    - `**kwargs`: Additional keyword arguments.
    """
    instance.customer.save()
