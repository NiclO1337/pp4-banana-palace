from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Table, Reservation
from home.models import Restaurant
from datetime import date
from .forms import PickDateForm
import random
# from django.contrib.auth import User



# create reservation page
@login_required
def reservation_page(request):

    test_user = User.objects.filter(id=3)
    table = Table.objects.filter(id=1000)
    restaurant = Restaurant.objects.filter(id=2)

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
        # If there are no tables then there are no reservation
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


    # if tables:
    #     tester = Reservation(
    #             user=test_user[0],
    #             party_size='4',
    #             table=table[0],
    #             restaurant=restaurant[0],
    #         )


    #     if not reservations:
    #         reservations = []
    #         for reservation in range(1):
    #             new_reservation = tester
    #             new_reservation.save()
    #             reservations.append(new_reservation)


    if request.method == "POST":
        date_form = PickDateForm(data=request.POST)
        if date_form.is_valid():
            selected_date = date_form.cleaned_data['date']
            tables = Table.objects.filter(date=selected_date)
            reservations = Reservation.objects.filter(
                table__date=selected_date)
            if not tables:
                tables = []
                for table in range(nr_of_tables):
                    new_table = Table(date=selected_date)
                    new_table.save()
                    tables.append(new_table)

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
                   'random_number': random_number,
                   'list_of_nums': list_of_nums,
                   'list_of_random_nums': list_of_random_nums,

                   })



# create automated bookings when selecting time to pre populate the
# bookings to create the appearance of existing bookings every day
# JavaScript? check PP2 get value from input and walkthrough project
# check rosie resume, github connection

# might be slow for user, create tables and pre-populate bookings
# when loading reservation page
# if reservations filter through each day
# for 30 days and if 0 = create 10 bookings








# edit reservation page, get ID, check customer edit.




# Delete reservation page, get ID, check request.user vs user

