from django.db import models
from django.contrib.auth.models import User
from home.models import Restaurant
from datetime import date


class Table(models.Model):

    # Do I acctually need date field on both models...
    # They are already OneToOneField...
    date = models.DateField(default=date.today)
    reserved = models.BooleanField(default=False)


class Reservation(models.Model):
    """
    Creates a reservation related to user, customer, table
    """

    PARTY_SIZE = ((0, '2'), (1, '3'), (2, '4'), (3, '5'),
                  (4, '6'), (5, '7'), (6, '8'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # date = models.DateField()
    time = models.TimeField(default="17:00")
    party_size = models.IntegerField(choices=PARTY_SIZE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    table = models.OneToOneField(Table, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    # Do not think I need this one since user is a FK and I should be able
    # to get it by targetting User.customer.has_discount

    # has_discount = models.BooleanField(default=False)