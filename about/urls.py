from django.urls import path
from . import views

# URL patterns for the 'about' app
urlpatterns = [
    # About page
    path('', views.About.as_view(), name='about'),

    # Our Story page
    path('story/', views.OurStory.as_view(), name='our-story'),

    # Terms and Conditions page
    path('terms-and-conditions/', views.TermsAndConditions.as_view(),
         name='terms-and-conditions'),

    # Privacy Policy page
    path('privacy-policy/', views.PrivacyPolicy.as_view(),
         name='privacy-policy'),

    # Cookie Policy page
    path('cookie-policy/', views.CookiePolicy.as_view(),
         name='cookie-policy'),

    # Modern Slavery Statement page
    path('modern-slavery-statement/', views.ModernSlaveryStatement.as_view(),
         name='modern-slavery-statement'),

    # Gender Pay Gap page
    path('gender-pay-gap/', views.GenderPayGap.as_view(),
         name='gender-pay-gap'),

    # Animal Welfare page
    path('animal-welfare/', views.AnimalWelfare.as_view(),
         name='animal-welfare'),

    # Investor Relations page
    path('investor-relations/', views.InvestorRelations.as_view(),
         name='investor-relations'),

    # Allergens page
    path('allergens/', views.Allergens.as_view(), name='allergens'),

    # Careers page
    path('careers/', views.Careers.as_view(), name='careers'),
]
