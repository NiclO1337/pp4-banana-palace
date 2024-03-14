from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Table
from datetime import date
# from django.contrib.auth import User




# create reservation page
@login_required
def reservation_page(request):

    nr_of_tables = request.user.customer.restaurant.avalible_tables

    today = date.today

    tables = Table.objects.filter()

    if not tables:
        for table in nr_of_tables:
            Table()
            table.save



    # tables = [
    #     Table(),
    # # ]
    # Table.objects.bulk_create(tables)




    return render(request, 'reservation/reservation.html',
                  {'range': range(nr_of_tables),
                   'tables': tables,
                   'today': today})




# create automated bookings when selecting time to pre populate the
# bookings to create the appearance of existing bookings every day
# JavaScript? check PP2 get value from input and walkthrough project
# check rosie resume, github connection

# might be slow for user, create tables and pre-populate bookings
# when loading reservation page
# if reservations filter through each day
# for 30 days and if 0 = create 10 bookings



# Create number of avalible tables from Restaurant model
# Get restaurant by name, get restarant.avalible_tables value
# Tables need specific position.

# or create finished tables with position in html with unique ID's,
# and create database tables from the html when choosing it

# Or create by model as planned and use JS to position them correctly,
# relative parent, absolute children.



"""
Continue as planned and learn from it
"""





# edit reservation page, get ID, check customer edit.




# Delete reservation page, get ID, check request.user vs user

