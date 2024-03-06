from django.conf.urls import path
from . import views

urlpatterns = [
    path('', views.About.as_view(), name='account'),
]