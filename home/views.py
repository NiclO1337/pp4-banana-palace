from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class Home(TemplateView):

    template_name = 'home/index.html'

