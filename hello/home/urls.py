from django.contrib import admin
from django.urls import path
from home import views
from django.urls import path
from . import views
from .views import contact_view
from django.urls import path



   





urlpatterns = [
    path('index',views.index, name='home'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
     path('contact/', contact_view, name='contact'),
    #path('success/', TemplateView.as_view(template_name="success.html"), name='success'),  # Add a success page
      
    
    path('destination/',views.destination, name='destination'),
    path('chandigarh/',views.chandigarh, name='chandigarh'),
    path('Delhi/',views.Delhi, name='Delhi'),
    path('haryana/',views.haryana, name='haryana'),
    path('himachal/',views.himachal_pradesh, name='himachal'),
    path('jammu/',views.jammu_kashmir, name='jammu'),
    path('ladakh/',views.ladakh, name='ladakh'),
    path('andaman/',views.andaman, name='andaman'),
    path('andra/',views.andra, name='andra'),
    path('kerala/',views.kerala, name='kerala'),
    path('karnataka/',views.karnataka, name='karnataka'),
    path('kerala/',views.kerala, name='kerala'),
    path('kerala/',views.kerala, name='kerala'),
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('hotel_booking/', views.hotel_booking, name='hotel_booking'),
    path('logout/', views.LogoutPage, name='logout'),
    path('flight-booking/', views.flight_booking_view, name='flight-booking'),
    path('success/',views.success_view, name='success'),
    path('paymentpage/',views.paymentpage, name='paymentpage'),
    path('successbook/',views.successbook, name='successbook'),
    path('location/',views.location, name='location'),
    
    
]



    

