from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class About(TemplateView):

    template_name = 'about/about.html'


class OurStory(TemplateView):

    template_name = 'about/our-story.html'


class TermsAndConditions(TemplateView):

    template_name = 'about/terms-and-conditions.html'


class PrivacyPolicy(TemplateView):

    template_name = 'about/privacy-policy.html'


class CookiePolicy(TemplateView):

    template_name = 'about/cookie-policy.html'


class ModernSlaveryStatement(TemplateView):

    template_name = 'about/modern-slavery-statement.html'


class GenderPayGap(TemplateView):

    template_name = 'about/gender-pay-gap.html'


class AnimalWelfare(TemplateView):

    template_name = 'about/animal-welfare.html'


class InvestorRelations(TemplateView):

    template_name = 'about/investor-relations.html'


class Allergens(TemplateView):

    template_name = 'about/allergens.html'


class Careers(TemplateView):

    template_name = 'about/careers.html'
