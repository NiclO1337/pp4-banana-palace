from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
            messages.error(request, 'Some field is incorrect and could not \
be submitted. See message next to relevant field.')

    else:
        user_form = EditUserForm(instance=request.user)
        customer_form = EditCustomerForm(instance=request.user.customer)


    return render(request, 'account/edit_account.html', {
        'user_form': user_form, 'customer_form': customer_form
        })


@login_required
def delete_account(request):

    if request.method == 'POST':

        delete_user = User.objects.get(username=request.user)

        delete_user.delete()
        messages.success(request, 'Your account has been deleted and your \
personal information removed from the database. Welcome back anytime!')
        return redirect(to='home')

    else:

        return render(request, 'account/delete_account.html')


@login_required
def fireworks_page(request):

    return render(request, 'account/fireworks.html')