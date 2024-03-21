from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class About(TemplateView):

    template_name = 'about/about.html'


class OurStory(TemplateView):

    template_name = 'about/our-story.html'


class TermsAndConditions(TemplateView):

    template_name = 'about/terms-and-conditions.html'
