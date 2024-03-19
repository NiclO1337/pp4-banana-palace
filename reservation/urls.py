from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_page, name='reservation_page'),
    path('<int:table_id>', views.reserve_table, name='reserve_table'),
]