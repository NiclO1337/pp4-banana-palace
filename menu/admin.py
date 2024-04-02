from django.contrib import admin
from .models import MenuItem

# Register the MenuItem model with the Django admin site
# This allows the model to be managed through the Django admin interface
admin.site.register(MenuItem)
