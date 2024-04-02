from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('about/', include('about.urls'), name='about-urls'),
    path('account/', include('customer.urls'), name='customer-urls'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls, name='admin:index'),
    path('menu/', include('menu.urls'), name='menu-urls'),
    path('reservation/', include('reservation.urls'), name='reservation-urls'),
    path('', include('home.urls'), name='home-urls'),
]
