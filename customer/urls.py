from django.urls import path
from . import views

# URL patterns for the account app
urlpatterns = [
    # Account page
    path('', views.account, name='account'),

    # Edit account page
    path('edit_account/', views.account_edit_view, name='edit_account'),

    # Delete account page
    path('delete_account/', views.delete_account, name='delete_account'),

    # Fireworks page
    path('surprice/', views.fireworks_page, name='fireworks_page'),

    # Change discount status for a user
    path('change_discount/<int:user_id>',
         views.change_discount, name='change_discount')
]
