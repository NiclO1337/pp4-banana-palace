from django.contrib import admin
from .models import Customer

# Register the Customer model with the admin site
# This allows the model to be managed through the Django admin interface
admin.site.register(Customer)
