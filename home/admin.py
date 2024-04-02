from django.contrib import admin
from .models import Restaurant

# Register the Restaurant model with the Django admin site
# This allows the model to be managed through the Django admin interface
admin.site.register(Restaurant)