from django.db import models

# Create your models here.
# models.py
from django.db import models

class ContactUs(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    from django.db import models


    from django.db import models

class HotelBookings(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    date_from = models.DateField()
    date_to= models.DateField()
    number_of_guest = models.IntegerField()

    def __str__(self):
        return self.name
    


class FlightBookings(models.Model):
    # Choices for Airports
    AIRPORT_CHOICES = [
        ('DEL', 'Delhi - Indira Gandhi International Airport'),
        ('BOM', 'Mumbai - Chhatrapati Shivaji Maharaj International Airport'),
        ('BLR', 'Bangalore - Kempegowda International Airport'),
        ('HYD', 'Hyderabad - Rajiv Gandhi International Airport'),
        ('MAA', 'Chennai - Chennai International Airport'),
        ('CCU', 'Kolkata - Netaji Subhas Chandra Bose International Airport'),
        ('AMD', 'Ahmedabad - Sardar Vallabhbhai Patel International Airport'),
        ('COK', 'Kochi - Cochin International Airport'),
        ('GOI', 'Goa - Goa International Airport'),
        ('PNQ', 'Pune - Pune International Airport'),
        ('ATQ', 'Amritsar - Sri Guru Ram Dass Jee International Airport'),
        ('JAI', 'Jaipur - Jaipur International Airport'),
        ('TRV', 'Thiruvananthapuram - Trivandrum International Airport'),
        ('LKO', 'Lucknow - Chaudhary Charan Singh International Airport'),
        ('VGA', 'Vijayawada - Vijayawada International Airport'),
        ('PAT', 'Patna - Jay Prakash Narayan International Airport'),
        ('GAU', 'Guwahati - Lokpriya Gopinath Bordoloi International Airport'),
        ('SXR', 'Srinagar - Sheikh ul-Alam International Airport'),
        ('BBI', 'Bhubaneswar - Biju Patnaik International Airport'),
        # Add more airports as needed
    ]

    # Choices for Preferred Airlines
    AIRLINE_CHOICES = [
        ('IndiGo', 'IndiGo'),
        ('AirIndia', 'AirIndia'),
        ('SpiceJet', 'SpiceJet'),
    ]

    # Choices for Preferred Seating
    SEATING_CHOICES = [
        ('Economy', 'Economy Class'),
        ('Business', 'Business Class'),
        ('First', 'First Class'),
    ]

    # Choices for Trip Type
    TRIP_TYPE_CHOICES = [
        ('one_way', 'One Way'),
        ('round_trip', 'Round Trip'),
    ]

    from_airport = models.CharField(max_length=3, choices=AIRPORT_CHOICES)
    to_airport = models.CharField(max_length=3, choices=AIRPORT_CHOICES)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    preferred_airlines = models.CharField(max_length=50, choices=AIRLINE_CHOICES, blank=True, null=True)
    preferred_seating = models.CharField(max_length=50, choices=SEATING_CHOICES, blank=True, null=True)
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField(blank=True, null=True)
    infants = models.PositiveIntegerField(blank=True, null=True)
    trip_type = models.CharField(max_length=10, choices=TRIP_TYPE_CHOICES)
    return_date = models.DateField(blank=True, null=True)
    return_time = models.TimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.full_name} - {self.from_airport} to {self.to_airport}"


   




   
    
    
    


    