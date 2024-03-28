from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem
from .forms import MenuItemForm
from django.contrib import messages


# Create your views here.
def menu_page(request):

    starters = MenuItem.objects.filter(category='Starters').filter(
        is_current=True).order_by('price')
    mains = MenuItem.objects.filter(category='Mains').filter(
        is_current=True).order_by('price')
    desserts = MenuItem.objects.filter(category='Desserts').filter(
        is_current=True).order_by('price')
    drinks = MenuItem.objects.filter(category='Drinks').filter(
        is_current=True).order_by('price')
    kids = MenuItem.objects.filter(category='Kids').filter(
        is_current=True).order_by('price')

    inactives = MenuItem.objects.filter(is_current=False)

    return render(request, 'menu/menu.html', {
        'starters': starters,
        'mains': mains,
        'desserts': desserts,
        'drinks': drinks,
        'kids': kids,
        'inactives': inactives,
    })


def add_menu_item(request):

    if request.method == 'POST':

        menu_item_form = MenuItemForm(request.POST, request.FILES)

        if menu_item_form.is_valid() and request.user.is_staff:
            menu_item_form.save()
            messages.success(request, 'Menu item added successfully!')
            return redirect('menu_page')
        else:
            messages.error(request, 'Something went wrong!')

    else:
        menu_item_form = MenuItemForm(initial={'is_current': True})

    return render(request, 'menu/add-menu-item.html', {
        'menu_item_form': menu_item_form,
    })


def edit_menu_item(request, menu_item_id):

    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)

    if request.method == 'POST':

        menu_item_form = MenuItemForm(
            request.POST, request.FILES, instance=menu_item)

        if menu_item_form.is_valid() and request.user.is_staff:
            menu_item_form.save()
            messages.success(request, 'Menu item updated successfully!')
            return redirect('menu_page')
        else:
            messages.error(request, 'Something went wrong!')

    else:
        menu_item_form = MenuItemForm(instance=menu_item)

    return render(request, 'menu/edit-menu-item.html', {
        'menu_item_form': menu_item_form,
    })


def delete_menu_item(request, menu_item_id):


    return render(request, 'menu/delete-menu-item.html',)

