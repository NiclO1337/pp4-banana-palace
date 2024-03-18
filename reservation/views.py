from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Table, Reservation
from datetime import date
from .forms import PickDateForm
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

        random_number = random.randint(10,20)
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

                random_number = random.randint(10,20)
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



# might be slow for user, create tables and pre-populate bookings
# when loading reservation page
# if reservations filter through each day
# for 30 days and if 0 = create 10 bookings



def reserve_table(request):



    return render(request, 'reservation/reserve_table.html')




# edit reservation page, get ID, check customer edit.




# Delete reservation page, get ID, check request.user vs user

