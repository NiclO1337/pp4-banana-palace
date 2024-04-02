from django.db import models
from django.contrib.auth.models import User
from home.models import Restaurant
from datetime import date, datetime, timedelta


class Table(models.Model):

    date = models.DateField(default=date.today)
    reserved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'Table ID: {self.id} - {self.date}'


class Reservation(models.Model):
    """
    Creates a reservation related to user, customer, table
    """

    TIME_CHOISES = []
    start_time = datetime.strptime('17:00', '%H:%M')
    end_time = datetime.strptime('21:15', '%H:%M')

    while start_time < end_time:

        start_time_slot = start_time.strftime('%H:%M')

        TIME_CHOISES.append((start_time_slot, start_time_slot))

        start_time += timedelta(minutes=15)

    PARTY_SIZE = ((2, '2'), (3, '3'), (4, '4'), (5, '5'),
                  (6, '6'), (7, '7'), (8, '8'))

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=5)
    time = models.CharField(max_length=15, choices=TIME_CHOISES,
                            default=TIME_CHOISES[0][0])
    party_size = models.IntegerField(choices=PARTY_SIZE, default=4)
    notes = models.TextField(null=True, blank=True, max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    table = models.OneToOneField(Table, on_delete=models.CASCADE, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   default=2)

    class Meta:
        ordering = ['table__date']

    def __str__(self):
        return f'Date: {self.table.date} ---- Party size: {self.party_size} \
---- Customer: {self.user.first_name} {self.user.last_name}. ---- \
Has discount: {self.user.customer.has_discount}'

    def save(self, *args, **kwargs):

        # Call original reservation save
        super(Reservation, self).save(*args, **kwargs)

        # Update associated table to be reserved
        self.table.reserved = True
        self.table.save(update_fields=['reserved'])

    def update(self, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
