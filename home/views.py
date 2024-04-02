from django.shortcuts import render
from menu.models import MenuItem


def home_page(request):
    """
    Display the home page with current menu items.

    **GET:**
    - Returns the home page with a list of current menu items.

    **Context:**
    - ``menu_items``: A queryset of :model:`menu.MenuItem`
    instances that are marked as current.

    **Template:**
    - :template:`home/index.html`
    """
    menu_items = MenuItem.objects.filter(is_current=True)

    return render(request, 'home/index.html', {'menu_items': menu_items,})
