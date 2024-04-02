from django.contrib import admin
from django.urls import path, include

# URL patterns for the project
urlpatterns = [
    # About app URLs
    path('about/', include('about.urls'), name='about-urls'),

    # Customer account URLs
    path('account/', include('customer.urls'), name='customer-urls'),

    # Authentication URLs provided by allauth
    path('accounts/', include('allauth.urls')),

    # Admin URLs
    path('admin/', admin.site.urls, name='admin:index'),

    # Menu app URLs
    path('menu/', include('menu.urls'), name='menu-urls'),

    # Reservation app URLs
    path('reservation/', include('reservation.urls'), name='reservation-urls'),

    # Home app URLs
    path('', include('home.urls'), name='home-urls'),
]
