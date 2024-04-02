from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    """
    Store a single restaurants information
    """
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    avalible_tables = models.IntegerField()

    def __str__(self):
        return f'Restaurant name: *{self.name}*'

