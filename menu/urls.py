from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuPage.as_view(), name='menu_page'),
    path('edit/', views.edit_menu_item, name='edit_menu_item'),
    path('add/', views.add_menu_item, name='add_menu_item'),
    path('delete/', views.delete_menu_item, name='delete_menu_item'),
]