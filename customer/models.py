from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from home.models import Restaurant


class Customer(models.Model):
    """
    Creates a customer related to :model:`auth.User`.

    This model represents a customer in the system, with a one-to-one
    relationship to the Django User model. It includes fields for discount
    status, click status, ownership status, phone number, and a foreign
    key to the Restaurant model.
    """
    # One-to-one relationship with the User model
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE
    )

    # Boolean fields indicating various customer statuses
    has_discount = models.BooleanField(default=False)
    has_clicked = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

    # Phone number field using the PhoneNumberField from phonenumber_field
    phone = PhoneNumberField()

    # Foreign key to the Restaurant model, with a
    # related_name for reverse lookups
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="customers",
        null=True, blank=True, default=2
    )

    def __str__(self):
        return str(self.user)
