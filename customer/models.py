from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    """
    Creates a customer related to :model:`auth.User`
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer"
    )
    has_discount = models.BooleanField(default=False)
    has_clicked = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)