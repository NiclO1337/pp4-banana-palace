from django.urls import path
from . import views

urlpatterns = [
    # Root URL for the reservation page
    path('', views.reservation_page, name='reservation_page'),

    # URL for reserving a specific table by its ID
    path('<int:table_id>', views.reserve_table, name='reserve_table'),

    # URL for editing a reservation by its ID
    path('edit/<int:reservation_id>',
         views.edit_reservation, name='edit_reservation'),

    # URL for editing a reservation and its associated table by their IDs
    path('edit/<int:reservation_id>/<int:table_id>',
         views.edit_reserve_table, name='edit_reserve_table'),

    # URL for deleting a reservation by its ID
    path('delete-reservation/<int:reservation_id>',
         views.delete_reservation, name='delete_reservation'),

    # URL for deleting old tables
    path('delete_old_tables', views.delete_old_tables,
         name='delete_old_tables'),
]
