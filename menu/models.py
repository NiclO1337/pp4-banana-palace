from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Menu(models.Model):

    CATEGORY_CHOICES = [
        ('Starters', 'Starters'),
        ('Mains', 'Mains'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks'),
        ('Kids', 'Kids'),
    ]

    title = models.CharField()
    content = models.TextField()
    price = MoneyField(max_digits=3, decimal_places=0, default_currency='EUR')
    category = models.CharField(choices=CATEGORY_CHOICES)
    image = models.ImageField()
    is_current = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)