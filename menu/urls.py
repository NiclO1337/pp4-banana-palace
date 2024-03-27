from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuPage.as_view(), name='menu_page'),
    path('edit/', views.edit_meal, name='edit_meal'),
    path('add/', views.add_meal, name='add_meal'),
    path('delete/', views.delete_meal, name='delete_meal'),
]