from menu.models import MenuItem
from django.shortcuts import render


def home_page(request):

    menu_items = MenuItem.objects.filter(is_current=True)

    return render(request, 'home/index.html', {'menu_items': menu_items,})
