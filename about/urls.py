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
    path('modern-slavery-statement/', views.ModernSlaveryStatement.as_view(),
         name='modern-slavery-statement'),
    path('gender-pay-gap/', views.GenderPayGap.as_view(),
         name='gender-pay-gap'),
    path('animal-welfare/', views.AnimalWelfare.as_view(),
         name='animal-welfare'),
    path('investor-relations/', views.InvestorRelations.as_view(),
         name='investor-relations'),
    path('allergens/', views.Allergens.as_view(),
         name='allergens'),
]