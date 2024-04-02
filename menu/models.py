from django.db import models
from djmoney.models.fields import MoneyField


class MenuItem(models.Model):

    CATEGORY_CHOICES = [
        ('Starters', 'Starters'),
        ('Mains', 'Mains'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks'),
        ('Kids', 'Kids'),
    ]

    title = models.CharField(max_length=50)
    content = models.TextField(max_length=150)
    price = MoneyField(max_digits=3, decimal_places=0, default_currency='EUR')
    category = models.CharField(choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='')
    is_current = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ----- {self.category} ----- {self.is_current}'
