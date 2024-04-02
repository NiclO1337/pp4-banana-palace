from django.contrib import admin
from .models import Table, Reservation

# Register the Table and Reservation models with the Django admin site
# This allows the models to be managed through the Django admin interface
admin.site.register(Table)
admin.site.register(Reservation)
