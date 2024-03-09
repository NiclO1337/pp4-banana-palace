from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditUserForm, EditCustomerForm

# Create your views here.
@login_required()
def account(request):
    """
    Display users account page
    """
    return render(request, 'account/account.html')


@login_required
def account_edit_view(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        customer_form = EditCustomerForm(request.POST,
                                        instance=request.user.customer)

        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            messages.success(request,
                             'Your account information updated succesfully')
            return redirect(to='account')
        else:
            messages.error(request,
                           'Something is wrong and could not be submitted')

    else:
        user_form = EditUserForm(instance=request.user)
        customer_form = EditCustomerForm(instance=request.user.customer)


    return render(request, 'account/edit_account.html', {
        'user_form': user_form, 'customer_form': customer_form
        })

