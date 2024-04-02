from django.views.generic import TemplateView


class About(TemplateView):
    """
    A view that renders the 'about/about.html' template.

    This view is used to display the About page of the website.
    """

    template_name = 'about/about.html'


class OurStory(TemplateView):
    """
    A view that renders the 'about/our-story.html' template.

    This view is used to display the Our Story page of the website.
    """

    template_name = 'about/our-story.html'


class TermsAndConditions(TemplateView):
    """
    A view that renders the 'about/terms-and-conditions.html' template.

    This view is used to display the Terms and Conditions page of the website.
    """
    template_name = 'about/terms-and-conditions.html'


class PrivacyPolicy(TemplateView):
    """
    A view that renders the 'about/privacy-policy.html' template.

    This view is used to display the Privacy Policy page of the website.
    """
    template_name = 'about/privacy-policy.html'


class CookiePolicy(TemplateView):
    """
    A view that renders the 'about/cookie-policy.html' template.

    This view is used to display the Cookie Policy page of the website.
    """
    template_name = 'about/cookie-policy.html'


class ModernSlaveryStatement(TemplateView):
    """
    A view that renders the 'about/modern-slavery-statement.html' template.

    This view is used to display the Modern Slavery Statement page of the website.
    """
    template_name = 'about/modern-slavery-statement.html'


class GenderPayGap(TemplateView):
    """
    A view that renders the 'about/gender-pay-gap.html' template.

    This view is used to display the Gender Pay Gap page of the website.
    """
    template_name = 'about/gender-pay-gap.html'


class AnimalWelfare(TemplateView):
    """
    A view that renders the 'about/animal-welfare.html' template.

    This view is used to display the Animal Welfare page of the website.
    """
    template_name = 'about/animal-welfare.html'


class InvestorRelations(TemplateView):
    """
    A view that renders the 'about/investor-relations.html' template.

    This view is used to display the Investor Relations page of the website.
    """
    template_name = 'about/investor-relations.html'


class Allergens(TemplateView):
    """
    A view that renders the 'about/allergens.html' template.

    This view is used to display the Allergens page of the website.
    """
    template_name = 'about/allergens.html'


class Careers(TemplateView):
    """
    A view that renders the 'about/careers.html' template.

    This view is used to display the Careers page of the website.
    """
    template_name = 'about/careers.html'
