from django.contrib import admin
from home.models import ContactUs
from home.models import FlightBookings
from home.models import HotelBookings


# Register your models here.
admin.site.register(ContactUs)
admin.site.register(FlightBookings)
admin.site.register(HotelBookings)

