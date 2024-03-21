from django.urls import path
from . import views

urlpatterns = [
    path('', views.About.as_view(), name='about'),
    path('story/', views.OurStory.as_view(), name='our-story'),
    path('terms-and-conditions/', views.TermsAndConditions.as_view(),
         name='terms'),
    path('privacy-policy/', views.PrivacyPolicy.as_view(),
         name='privacy-policy'),
    path('cookie-policy/', views.CookiePolicy.as_view(),
         name='cookie-policy'),
]