from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import ContactUs
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required
from home.models import HotelBookings

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')


def destination(request):
    return render(request,'destination.html')
def register(request):
    if request.method == 'POST':
        uname = request.POST.get('UserName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname, email, password)
        my_user.save()
        return redirect('login')  # Use the URL name 'login'

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login instead of login
            return redirect('home')
        else:
            return HttpResponse("Username or Password Is Incorrect")

    return render(request, 'login.html')
def LogoutPage(request):
    logout(request)
    return redirect('login')

    
def chandigarh(request):
    return render(request,'chandigarh.html')

def Delhi(request):
    return render(request,'Delhi.html')

def himachal_pradesh(request):
    return render(request,'himachal.html')

def jammu_kashmir(request):
    return render(request,'jammu.html')

def ladakh(request):
    return render(request,'ladakh.html')

def andaman(request):
    return render(request,'andaman.html')

def andra(request):
    return render(request,'andra.html')

def kerala(request):
    return render(request,'kerala.html')


def karnataka(request):
    return render(request,'karnataka.html')

def kerala(request):
    return render(request,'kerala.html')

def kerala(request):
    return render(request,'kerala.html')

def success_view(request):
    return render(request, 'flight_booking/success.html')

def haryana(request):
    return render(request,'haryana.html')

def about(request):
    return HttpResponse('this is about page')


def services(request):
    return HttpResponse('this is services page')

def rail(request):
    return render(request,'rail.html')


def success_view(request):
    return render(request, 'success.html')

def paymentpage(request):
    return render(request,'paymentpage.html')

def successbook(request):
    return render(request,'successbook.html')




def hotel_booking(request):
    if request.method=='POST':
        name=request.POST.get('name')
        place=request.POST.get('place')
        date_from=request.POST.get('date_from')
        date_to=request.POST.get('date_to')
        number_of_guest=request.POST.get('no.of_guest')
        hotel=HotelBookings(name=name,place=place,date_from=date_from,date_to=date_to,number_of_guest=number_of_guest)
        hotel.save()
        return redirect('paymentpage') 
    return render(request,'hotel_booking.html')



from django.shortcuts import render, redirect
# views.py
from django.shortcuts import render, redirect
from .models import ContactUs
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        ContactUs.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            message=message
        )
        return redirect('success')  # Redirect to a success page or a thank you page

    return render(request, 'contact.html')


def location(request):
    return render(request,'location.html')




from django.shortcuts import render, redirect
from .models import FlightBookings
from datetime import datetime

def flight_booking_view(request):
    if request.method == 'POST':
        from_airport = request.POST.get('from_airport')
        to_airport = request.POST.get('to_airport')
        departure_date = request.POST.get('departure_date')
        departure_time = request.POST.get('departure_time')
        preferred_airlines = request.POST.get('preferred_airlines')
        preferred_seating = request.POST.get('preferred_seating')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        infants = request.POST.get('infants')
        trip_type = request.POST.get('trip_type')
        return_date = request.POST.get('return_date')
        return_time = request.POST.get('return_time')
        message = request.POST.get('message')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        
        departure_date = datetime.strptime(departure_date, '%d-%m-%Y').date() if departure_date else None
        return_date = datetime.strptime(return_date, '%d-%m-%Y').date() if return_date else None
        departure_time = datetime.strptime(departure_time, '%H:%M').time() if departure_time else None
        return_time = datetime.strptime(return_time, '%H:%M').time() if return_time else None

        flight_booking = FlightBookings(
            from_airport=from_airport,
            to_airport=to_airport,
            departure_date=departure_date,
            departure_time=departure_time,
            preferred_airlines=preferred_airlines,
            preferred_seating=preferred_seating,
            adults=adults,
            children=children,
            infants=infants,
            trip_type=trip_type,
            return_date=return_date,
            return_time=return_time,
            message=message,
            full_name=full_name,
            phone_number=phone_number,
            email=email
        )

        flight_booking.save()
        return redirect('paymentpage') 
           # Redirect to a success page or a thank you page

        

    return render(request, 'flight_booking.html')
