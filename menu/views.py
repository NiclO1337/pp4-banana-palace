from django.shortcuts import render
from django.views import generic
from home.models import Restaurant

# Create your views here.
class MenuPage(generic.ListView):

    queryset = Restaurant.objects.all()
    template_name = 'menu/menu.html'


def add_meal(request):

    return render(request, 'menu/add_meal.html')


def edit_meal(request, meal_id):



    return render(request, 'menu/edit_meal.html',)