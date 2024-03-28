from django.shortcuts import render, redirect
from django.views import generic
from .models import MenuItem
from .forms import MenuItemForm
from django.contrib import messages


# Create your views here.
class MenuPage(generic.ListView):

    queryset = MenuItem.objects.all()
    template_name = 'menu/menu.html'


def add_menu_item(request):

    if request.method == 'POST':

        menu_item_form = MenuItemForm(request.POST, request.FILES)

        if menu_item_form.is_valid() and request.user.is_staff:
            menu_item_form.save()
            messages.success(request, 'Woohoo')
            return redirect('menu_page')
        else:
            messages.error(request, 'Naehae')

    else:
        menu_item_form = MenuItemForm(initial={'is_current': True})

    return render(request, 'menu/add-menu-item.html', {
        'menu_item_form': menu_item_form,
    })


def edit_menu_item(request, meal_id):


    return render(request, 'menu/edit-menu-item.html',)


def delete_menu_item(request, meal_id):


    return render(request, 'menu/delete-menu-item.html',)

