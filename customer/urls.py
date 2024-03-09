from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('edit_account/', views.account_edit_view, name='edit_account'),
]