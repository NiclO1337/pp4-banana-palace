# Generated by Django 5.0.2 on 2024-03-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_alter_table_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='party_size',
            field=models.IntegerField(choices=[(2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=0),
        ),
    ]
