from django import forms


# List of Indian airports
INDIAN_AIRPORTS = [
    ('DEL', 'Indira Gandhi International Airport, Delhi'),
    ('BOM', 'Chhatrapati Shivaji Maharaj International Airport, Mumbai'),
    ('BLR', 'Kempegowda International Airport, Bangalore'),
    ('MAA', 'Chennai International Airport, Chennai'),
    ('HYD', 'Rajiv Gandhi International Airport, Hyderabad'),
    ('CCU', 'Netaji Subhas Chandra Bose International Airport, Kolkata'),
    ('GOI', 'Goa International Airport, Goa'),
    ('AMD', 'Sardar Vallabhbhai Patel International Airport, Ahmedabad'),
    ('COK', 'Cochin International Airport, Kochi'),
    ('PNQ', 'Pune Airport, Pune'),
    # Add more airports as needed
]

class FlightBookingForm(forms.Form):
    from_location = forms.ChoiceField(choices=INDIAN_AIRPORTS, label="From")
    to_location = forms.ChoiceField(choices=INDIAN_AIRPORTS, label="To")
    departure_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    departure_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))
    preferred_airlines = forms.ChoiceField(choices=[
        ('IndoGo', 'IndoGo'),
        ('AirIndia', 'AirIndia'),
        ('Spacejet', 'Spacejet')
    ])
    preferred_seating = forms.ChoiceField(choices=[
        ('Economy', 'Economy Class'),
        ('Business', 'Business Class'),
        ('First', 'First Class')
    ])
    adult = forms.IntegerField(min_value=1)
    children = forms.IntegerField(min_value=0)
    infant = forms.IntegerField(min_value=0)
    trip_type = forms.ChoiceField(choices=[
        ('one_way', 'One Way'),
        ('round_trip', 'Round Trip')
    ], widget=forms.RadioSelect)
    return_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    return_time = forms.TimeField(required=False, widget=forms.TextInput(attrs={'type': 'time'}))
    message = forms.CharField(widget=forms.Textarea, required=False)
    full_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField()
