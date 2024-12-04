from django import forms
from .models import Contactme

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactme
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']
