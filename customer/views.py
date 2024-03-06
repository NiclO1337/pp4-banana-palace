from django.shortcuts import render

# Create your views here.
def account(request):
    """
    Display users account page
    """
    return render(request, 'customer/account.html')