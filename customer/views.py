from django.shortcuts import render

# Create your views here.
def Account(request):
    """
    Display users account page
    """
    return render(request, 'account/account.html')