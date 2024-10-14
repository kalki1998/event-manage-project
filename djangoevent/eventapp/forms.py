from django import forms 
from .models import booking

class DateInput(forms.DateInput):
    input_type ='date'

class Bookingform(forms.ModelForm):
    
    class Meta:
        model = booking
        fields = '__all__'
        widgets = {
            'booking_date': DateInput(),
        }
        labels = {
        'name':"username:",
        'event_name':"select event:",
        'booking_date':"select date:",
    }