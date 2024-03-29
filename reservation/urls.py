from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_page, name='reservation_page'),
    path('<int:table_id>', views.reserve_table, name='reserve_table'),

    path('edit/<int:reservation_id>',
         views.edit_reservation, name='edit_reservation'),
    path('edit/<int:reservation_id>/<int:table_id>',
         views.edit_reserve_table, name='edit_reserve_table'),

    path('delete-reservation/<int:reservation_id>',
         views.delete_reservation, name='delete_reservation'),

    path('delete_old_tables', views.delete_old_tables,
         name='delete_old_tables'),
]