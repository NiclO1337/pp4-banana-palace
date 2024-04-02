from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from reservation.models import Reservation
from reservation.models import Table
from .forms import EditUserForm, EditCustomerForm


@login_required()
def account(request):
    """
    Display users account page.

    **Context:**

    ``reservations``
        A queryset of :model:`reservation.Reservation` instances
        for the current user that are for tables with a date greater
        than or equal to today.
    ``all_users``
        A queryset of all :model:`auth.User` instances, ordered by
        their last login date in descending order.
    ``tables``
        A queryset of :model:`reservation.Table` instances with a date
        less than today, indicating they are in the past.

    **Template:**

    :template:`account/account.html`
    """
    all_users = User.objects.all().order_by('-last_login')

    today = timezone.now().date()

    tables = Table.objects.filter(date__lt=today)

    reservations = Reservation.objects.filter(
        user=request.user, table__date__gte=today)

    return render(request, 'account/account.html',
                  {'reservations': reservations,
                   'all_users': all_users,
                   'tables': tables})


@login_required
def account_edit_view(request):
    """
    View for editing user account information.

    **Context:**

    ``user_form``
        An instance of :form:`EditUserForm` for the current user.
    ``customer_form``
        An instance of :form:`EditCustomerForm` for the
        current user's customer profile.

    **Template:**

    :template:`account/edit_account.html`
    """
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
    """
    View for deleting a user account.

    **Template:**

    :template:`account/delete_account.html`
    """

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
    """
    View for updating a user's customer profile to indicate
    they have clicked on the discount button.

    **Template:**

    :template:`account/fireworks.html`
    """
    user = request.user

    user.customer.has_clicked = "True"
    user.save()

    return render(request, 'account/fireworks.html')


@login_required
def change_discount(request, user_id):
    """

    View for toggling a user's discount status.

    """
    user = User.objects.get(id=user_id)

    if request.user.customer.is_owner:
        if user.customer.has_discount:
            user.customer.has_discount = False
            user.save()
        else:
            user.customer.has_discount = True
            user.save()

        messages.success(request, f'Discount status changed on <br>\
{user.first_name} {user.last_name}')

    else:
        messages.error(request, f'You do not have permission to change this \
{request.user.first_name} {request.user.last_name}.')

    return redirect(to='account')
