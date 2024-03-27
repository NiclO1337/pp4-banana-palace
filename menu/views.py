from django.shortcuts import render
from django.views import generic
from .models import Menu

# Create your views here.
class MenuPage(generic.ListView):

    queryset = Menu.objects.all()
    template_name = 'menu/menu.html'


def add_menu_item(request):

    return render(request, 'menu/add_menu_item.html')


def edit_menu_item(request, meal_id):


    return render(request, 'menu/edit_menu_item.html',)


def delete_menu_item(request, meal_id):


    return render(request, 'menu/delete_menu_item.html',)

