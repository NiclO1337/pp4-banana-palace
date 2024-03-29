from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('edit_account/', views.account_edit_view, name='edit_account'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('surprice/', views.fireworks_page, name='fireworks_page'),

    path('change_discount/<int:user_id>',
         views.change_discount, name='change_discount')
]