# Generated by Django 5.0.2 on 2024-03-15 18:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_remove_reservation_date_reservation_time_table_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Select date'),
        ),
    ]
