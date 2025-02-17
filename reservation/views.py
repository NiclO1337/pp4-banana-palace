import random
from datetime import datetime
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Table, Reservation, Restaurant
from .forms import PickDateForm, ReserveTableForm
from customer.forms import EditUserFormReservation, EditCustomerForm


def reservation_page(request):
    """
    View for managing table reservations.

    **GET:**
    - Renders the reservation page with available tables and reservations
    for the current date.
    - If the user is authenticated, it fetches the number of available tables
    from the user's restaurant.
    - If no tables are available for the current date, it creates new tables
    and reservations based on a random number of reservations.

    **POST:**
    - Handles the submission of a date selection form. It filters tables and
    reservations based on the selected date.
    - If no tables are available for the selected date, it creates new tables
    and reservations based on a random number of reservations.

    **Context:**
    - ``tables``: A queryset of :model:`Table` instances available for the
    current or selected date.

    - ``date_form``: An instance of :form:`PickDateForm` for selecting a date.

    - ``reservations``: A queryset of :model:`Reservation` instances for
    the current or selected date.

    **Template:**
    - :template:`reservation/reservation.html`
    """
    if request.user.is_authenticated:
        nr_of_tables = request.user.customer.restaurant.avalible_tables

    else:
        restaurant = Restaurant.objects.all().first()
        nr_of_tables = restaurant.avalible_tables

    tables = Table.objects.filter(date=date.today()).order_by('id')
    reservations = Reservation.objects.filter(table__date=date.today())

    if not tables:
        tables = []
        for table in range(nr_of_tables):
            new_table = Table()
            new_table.save()
            tables.append(new_table)

        reservations = []

        random_number = random.randint(20, 40)
        list_of_nums = list(range(1, nr_of_tables))
        random.shuffle(list_of_nums)
        list_of_random_nums = []
        for num in range(random_number):
            random_num = list_of_nums[num]
            list_of_random_nums.append(random_num)

        for table in list_of_random_nums:
            new_reservation = Reservation(table=tables[table])
            new_reservation.save()
            reservations.append(new_reservation)

    if request.method == "POST":
        date_form = PickDateForm(data=request.POST)
        if date_form.is_valid():
            selected_date = date_form.cleaned_data['date']
            tables = Table.objects.filter(date=selected_date).order_by('id')
            reservations = Reservation.objects.filter(
                table__date=selected_date)
            if not tables:
                tables = []
                for table in range(nr_of_tables):
                    new_table = Table(date=selected_date)
                    new_table.save()
                    tables.append(new_table)

                reservations = []

                random_number = random.randint(20, 40)
                list_of_nums = list(range(1, nr_of_tables))
                random.shuffle(list_of_nums)
                list_of_random_nums = []
                for num in range(random_number):
                    random_num = list_of_nums[num]
                    list_of_random_nums.append(random_num)

                for table in list_of_random_nums:
                    new_reservation = Reservation(table=tables[table])
                    new_reservation.save()
                    reservations.append(new_reservation)

            return render(request, 'reservation/reservation.html',
                          {'tables': tables,
                           'date_form': date_form,
                           'reservations': reservations,
                           })

    date_form = PickDateForm()

    return render(request, 'reservation/reservation.html',
                  {'tables': tables,
                   'date_form': date_form,
                   'reservations': reservations,
                   })


@login_required
def reserve_table(request, table_id):
    """
    View for reserving a table.

    **POST:**
    - Handles the submission of forms for user and customer information, as
    well as the reservation form. If the table is already reserved or any of
    the forms are invalid, an error message is displayed. Otherwise, the
    reservation is completed, and a success message is shown.

    **GET:**
    - Renders the reservation form for the specified table,
    along with forms for editing user and customer information.

    **Context:**
    - ``table``: The :model:`Table` instance to be reserved.

    - ``reserve_table_form``: An instance of :form:`ReserveTableForm`
    for reserving the table.

    - ``user_form``: An instance of :form:`EditUserFormReservation`
    for editing user information.

    - ``customer_form``: An instance of :form:`EditCustomerForm`
    for editing customer information.

    **Template:**
    - :template:`reservation/reserve-table.html`
    """
    table = get_object_or_404(Table, pk=table_id)

    if request.method == 'POST':
        user_form = EditUserFormReservation(request.POST,
                                            instance=request.user)
        customer_form = EditCustomerForm(request.POST,
                                         instance=request.user.customer)
        reserve_table_form = ReserveTableForm(request.POST,
                                              request=request, table=table)

        if table.reserved:
            messages.error(request,
                           'This table has already been reserved, please \
choose another table')
            return redirect('reservation_page')

        elif user_form.is_valid() and customer_form.is_valid() and \
                reserve_table_form.is_valid():
            reservation = reserve_table_form.save(commit=False)
            reservation.user = request.user
            user_form.save()
            customer_form.save()
            reserve_table_form.save()

            messages.success(request, 'Reservation completed successfully')
            return redirect('account')

        else:
            messages.error(request, 'Form is not valid, please enter all \
necessairy information below')

    else:
        user_form = EditUserFormReservation(instance=request.user)
        customer_form = EditCustomerForm(instance=request.user.customer)
        reserve_table_form = ReserveTableForm(initial={
            'party_size': 4,
        })

    return render(request, 'reservation/reserve-table.html',
                  {'table': table,
                   'reserve_table_form': reserve_table_form,
                   'user_form': user_form,
                   'customer_form': customer_form,
                   })


@login_required
def edit_reservation(request, reservation_id):
    """
    View for editing an existing reservation.

    **POST:**
    - Handles the submission of a date selection form. It filters tables
    and reservations based on the selected date.
    - If no tables are available for the selected date, it creates new
    tables and reservations based on a random number of reservations.

    **GET:**
    - Renders the reservation edit page with the current
    reservation details and a form for selecting a new date.

    **Context:**
    - ``tables``: A queryset of :model:`Table` instances
    available for the current or selected date.

    - ``date_form``: An instance of :form:`PickDateForm`
    for selecting a new date.

    - ``reservations``: A queryset of :model:`Reservation`
    instances for the current or selected date.

    - ``reservation``: The :model:`Reservation` instance to be edited.

    **Template:**
    - :template:`reservation/edit-reservation.html`
    """
    nr_of_tables = request.user.customer.restaurant.avalible_tables
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    Table.objects.filter(id=reservation.table.id).update(reserved=False)

    tables = Table.objects.filter(date=reservation.table.date).order_by('id')
    reservations = Reservation.objects.filter(
        table__date=reservation.table.date)

    if request.method == "POST":
        date_form = PickDateForm(data=request.POST)
        if date_form.is_valid():
            selected_date = date_form.cleaned_data['date']
            tables = Table.objects.filter(date=selected_date).order_by('id')
            reservations = Reservation.objects.filter(
                table__date=selected_date)

            if not tables:
                tables = []
                for table in range(nr_of_tables):
                    new_table = Table(date=selected_date)
                    new_table.save()
                    tables.append(new_table)

                reservations = []

                random_number = random.randint(20, 40)
                list_of_nums = list(range(1, nr_of_tables))
                random.shuffle(list_of_nums)
                list_of_random_nums = []
                for num in range(random_number):
                    random_num = list_of_nums[num]
                    list_of_random_nums.append(random_num)

                for table in list_of_random_nums:
                    new_reservation = Reservation(table=tables[table])
                    new_reservation.save()
                    reservations.append(new_reservation)

            return render(request, 'reservation/edit-reservation.html',
                          {'tables': tables,
                           'date_form': date_form,
                           'reservations': reservations,
                           'reservation': reservation,
                           })

    date_form = PickDateForm(initial={
            'date': reservation.table.date, })

    return render(request, 'reservation/edit-reservation.html',
                  {'tables': tables,
                   'date_form': date_form,
                   'reservations': reservations,
                   'reservation': reservation,
                   })


@login_required
def edit_reserve_table(request, table_id, reservation_id):
    """
    View for editing an existing table reservation.

    **POST:**
    - Handles the submission of forms for user and customer information, as
    well as the reservation form. If the table is already reserved or any of
    the forms are invalid, an error message is displayed. Otherwise,
    the reservation is updated, and a success message is shown.

    **GET:**
    - Renders the reservation edit form for the specified table and
    reservation, along with forms for editing user and customer information.

    **Context:**
    - ``table``: The :model:`Table` instance associated with the reservation.

    - ``reservation``: The :model:`Reservation` instance to be edited.

    - ``reserve_table_form``: An instance of :form:`ReserveTableForm`
    for editing the reservation.

    - ``user_form``: An instance of :form:`EditUserFormReservation`
    for editing user information.

    - ``customer_form``: An instance of :form:`EditCustomerForm`
    for editing customer information.

    **Template:**
    - :template:`reservation/edit-reserve-table.html`
    """

    table = get_object_or_404(Table, pk=table_id)
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        user_form = EditUserFormReservation(request.POST,
                                            instance=reservation.user)
        customer_form = EditCustomerForm(request.POST,
                                         instance=reservation.user.customer)
        reserve_table_form = ReserveTableForm(request.POST, table=table,
                                              instance=reservation)

        if table.reserved:
            messages.error(request,
                           'This table has already been reserved, please \
choose another table')
            return redirect('account')

        elif user_form.is_valid() and customer_form.is_valid() and \
                reserve_table_form.is_valid() and \
                reservation.user == request.user:
            user_form.save()
            customer_form.save()
            reserve_table_form.save()

            messages.success(request, 'Reservation updated successfully')
            return redirect('account')

        else:
            messages.error(request, 'Form is not valid, please enter all \
necessairy information below')

    else:
        user_form = EditUserFormReservation(instance=reservation.user)
        customer_form = EditCustomerForm(instance=reservation.user.customer)
        reserve_table_form = ReserveTableForm(
            instance=reservation, initial={'time': reservation.time})

    return render(request, 'reservation/edit-reserve-table.html',
                  {'table': table,
                   'reservation': reservation,
                   'reserve_table_form': reserve_table_form,
                   'user_form': user_form,
                   'customer_form': customer_form,
                   })


def delete_reservation(request, reservation_id):
    """
    View for deleting an existing reservation.

    **POST:**
    - Handles the deletion of a reservation. If the reservation belongs to
    the current user, the reservation is deleted, the table is marked as not
    reserved, and a success message is displayed. Otherwise,
    an error message is displayed.

    **GET:**
    - Renders the confirmation page for deleting a reservation.

    **Context:**
    - ``reservation``: The :model:`Reservation` instance to be deleted.

    **Template:**
    - :template:`reservation/delete_reservation.html`
    """
    if request.method == 'POST':

        reservation = get_object_or_404(Reservation, pk=reservation_id)

        if reservation.user == request.user:
            reservation.table.reserved = False
            reservation.table.save()
            reservation.delete()
            messages.success(request, 'Your reservation has been successfully \
deleted. We hope to see you soon!')
        else:
            messages.error(request, 'Something went wrong, please \
try again or contact our support.')

        return redirect(to='account')

    else:
        return render(request, 'reservation/delete_reservation.html')


@login_required
def delete_old_tables(request):
    """
    View for deleting tables that are no longer needed.

    **GET:**
    - Deletes all tables with a date less than the current date.
    If the user is an owner, all such tables are deleted.

    **Context:**
    - ``tables``: A queryset of :model:`Table` instances to be deleted.
    """
    current_date = datetime.now().date()

    tables = Table.objects.filter(date__lt=current_date)

    if request.user.customer.is_owner:
        for table in tables:
            table.delete()

    return redirect('account')
