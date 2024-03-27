from django.shortcuts import render, redirect
from django.views import generic
from .models import Menu
from .forms import MenuItemForm
from django.contrib import messages


# Create your views here.
class MenuPage(generic.ListView):

    queryset = Menu.objects.all()
    template_name = 'menu/menu.html'


def add_menu_item(request):

    if request.method == 'POST':

        menu_item_form = MenuItemForm(request.POST, instance=request.user)

        if menu_item_form.is_valid() and request.user.is_staff:
            menu_item_form.save()
            messages.SUCCESS(request, 'Woohoo')
            redirect('menu_page')
        else:
            messages.ERROR(request, 'Naehae')

    else:
        menu_item_form = MenuItemForm(instance=request.user)

    return render(request, 'menu/add-menu-item.html', {
        'menu_item_form': menu_item_form,
    })


def edit_menu_item(request, meal_id):


    return render(request, 'menu/edit-menu-item.html',)


def delete_menu_item(request, meal_id):


    return render(request, 'menu/delete-menu-item.html',)

