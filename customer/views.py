from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
@login_required()
def account(request):
    """
    Display users account page
    """
    return render(request, 'account/account.html')

class AccountEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'account/edit_account.html'
    success_url = reverse_lazy('account')

    def get_object(self):
        return self.request.user