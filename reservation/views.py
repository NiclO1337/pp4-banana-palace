from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Table
from datetime import date
from .forms import PickDateForm
# from django.contrib.auth import User




# create reservation page
@login_required
def reservation_page(request):


    # Get number of avalible tables from the resturant
    # associated with the logged in user
    nr_of_tables = request.user.customer.restaurant.avalible_tables

    # get all tables for todays date (today is when page is loaded)
    tables = Table.objects.filter(date=date.today())

    # if there are no tables, create tables and save them to the database
    # nr of tables created depends on restaurants nr of avalible tables
    if not tables:
        for table in range(nr_of_tables):
            new_table = Table()
            new_table.save()
            tables.append(new_table)


    if request.method == "POST":
        date_form = PickDateForm(data=request.POST)

    date_form = PickDateForm()

    return render(request, 'reservation/reservation.html',
                  {'tables': tables,
                   'date_form': date_form,
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

