from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_page, name='menu_page'),
    path('', views.edit_menu, name='edit_menu'),
]