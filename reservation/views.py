from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Table, Reservation
from datetime import date
from .forms import PickDateForm, ReserveTableForm
from customer.forms import EditUserFormReservation, EditCustomerForm
import random


@login_required
def reservation_page(request):

    # Get number of avalible tables from the resturant
    # associated with the logged in user
    nr_of_tables = request.user.customer.restaurant.avalible_tables

    # get all tables and reservations for todays date
    # (today is when page is loaded)
    tables = Table.objects.filter(date=date.today()).order_by('id')
    reservations = Reservation.objects.filter(table__date=date.today())

    # if there are no tables, create tables and save them to the database
    # nr of tables created depends on restaurants nr of avalible tables
    if not tables:
        tables = []
        for table in range(nr_of_tables):
            new_table = Table()
            new_table.save()
            tables.append(new_table)

        # If there are no tables then there are no reservations.
        # Pre-populate reservations to make it look realistic
        reservations = []

        random_number = random.randint(20,40)
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

                random_number = random.randint(20,40)
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

    table = get_object_or_404(Table, pk=table_id)

    if request.method == 'POST':
        user_form = EditUserFormReservation(request.POST,
                                            instance=request.user)
        customer_form = EditCustomerForm(request.POST,
                                        instance=request.user.customer)
        reserve_table_form = ReserveTableForm(request.POST,
                                              request=request, table=table)
        if table.reserved:
            # Check if table is reserved incase user cheated with URL.
            messages.error(request,
                           'This table has already been reserved, please \
choose another table')
            return redirect('reservation_page')

        elif reserve_table_form.is_valid():
            user_form.save()
            customer_form.save()
            reserve_table_form.save()

            # Redirect account page and display success message.
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




# edit reservation page, get ID, check customer edit.
@login_required
def edit_reservation(request, reservation_id):

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

                random_number = random.randint(20,40)
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
            'date': reservation.table.date,})

    return render(request, 'reservation/edit-reservation.html',
                  {'tables': tables,
                   'date_form': date_form,
                   'reservations': reservations,
                   'reservation': reservation,
                   })


def edit_reserve_table(request, table_id, reservation_id):

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
            # Check if table is reserved incase user cheated with URL.
            messages.error(request,
                           'This table has already been reserved, please \
choose another table')
            return redirect('reservation_page')

        elif user_form.is_valid() and customer_form.is_valid() and \
            reserve_table_form.is_valid() and reservation.user == request.user:
            user_form.save()
            customer_form.save()
            reserve_table_form.save()

            # Redirect account page and display success message.
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


# Delete reservation page, get ID, check request.user vs user

