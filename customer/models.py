from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from home.models import Restaurant

# Create your models here.
class Customer(models.Model):
    """
    Creates a customer related to :model:`auth.User`
    """
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE
    )
    has_discount = models.BooleanField(default=False)
    has_clicked = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    phone = PhoneNumberField()

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="customers",
        null=True, blank=True, default=2
    )


    def __str__(self):
        return str(self.user)