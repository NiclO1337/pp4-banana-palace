import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MenuItem
from .forms import MenuItemForm


def menu_page(request):
    """
    Display the menu page with categorized menu items.

    **GET:**
    - Returns the menu page with categorized menu items: Starters,
    Mains, Desserts, Drinks, Kids, and Inactive items.

    **Context:**
    - ``starters``: A queryset of :model:`menu.MenuItem` instances categorized
    as 'Starters' and marked as current, ordered by price.

    - ``mains``: A queryset of :model:`menu.MenuItem` instances categorized as
    'Mains' and marked as current, ordered by price.

    - ``desserts``: A queryset of :model:`menu.MenuItem` instances categorized
    as 'Desserts' and marked as current, ordered by price.

    - ``drinks``: A queryset of :model:`menu.MenuItem` instances categorized
    as 'Drinks' and marked as current, ordered by price.

    - ``kids``: A queryset of :model:`menu.MenuItem` instances categorized as
    'Kids' and marked as current, ordered by price.

    - ``inactives``: A queryset of :model:`menu.MenuItem` instances marked as
    not current.

    **Template:**
    - :template:`menu/menu.html`
    """
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


@login_required
def add_menu_item(request):
    """
    View for adding a new menu item.

    **POST:**
    - Handles the submission of a new menu item form. If the form is valid and
    the user is a staff member, the menu item is saved, and a success message
    is displayed. Otherwise, an error message is displayed.

    **GET:**
    - Renders the form for adding a new menu item with
    the 'is_current' field initially set to True.

    **Context:**
    - ``menu_item_form``: An instance of :form:`MenuItemForm`
    for adding a new menu item.

    **Template:**
    - :template:`menu/add-menu-item.html`
    """
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


@login_required
def edit_menu_item(request, menu_item_id):
    """
    View for editing an existing menu item.

    **POST:**
    - Handles the submission of an edit menu item form. If the form is valid
    and the user is a staff member, the menu item is updated, and a success
    message is displayed. Otherwise, an error message is displayed.

    **GET:**
    - Renders the form for editing an existing menu item.

    **Context:**
    - ``menu_item_form``: An instance of :form:`MenuItemForm`
    for editing an existing menu item.

    **Template:**
    - :template:`menu/edit-menu-item.html`
    """
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


@login_required
def delete_menu_item(request, menu_item_id):
    """
    View for deleting an existing menu item.

    **POST:**
    - Handles the deletion of a menu item. If the user is the owner and the
    menu item has an image, the image is removed from the filesystem before
    the menu item is deleted. A success message is displayed upon successful
    deletion. Otherwise, an error message is displayed.

    **Template:**
    - :template:`menu/delete-menu-item.html`
    """
    if request.method == 'POST':

        menu_item = get_object_or_404(MenuItem, pk=menu_item_id)

        if request.user.customer.is_owner:
            if menu_item.image:
                os.remove(menu_item.image.path)
            menu_item.delete()
            messages.success(request, 'Menu item deleted successfully!')
            return redirect('menu_page')
        else:
            messages.error(
                request, 'You do not have permission to perform this action!')

    return render(request, 'menu/delete-menu-item.html',)
