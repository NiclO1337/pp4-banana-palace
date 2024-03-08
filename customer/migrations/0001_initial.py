# Generated by Django 5.0.2 on 2024-03-06 03:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_discount', models.BooleanField(default=False)),
                ('has_clicked', models.BooleanField(default=False)),
                ('is_owner', models.BooleanField(default=False)),
                ('phone', models.IntegerField()),
                ('restaurant', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='home.restaurant')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]