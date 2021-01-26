from django.forms import ModelForm
from django import forms
from django.forms.widgets import DateInput, TimeInput, Select
from .models import Booking

class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'
		exclude = ['date_created', 'availability']
		widgets = {
		}



class JobBookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'
		exclude = ['date_created', 'availability']
		widgets = {
		#Hide All Fields in The Form
			'educator':forms.HiddenInput(),
			'manager':forms.HiddenInput(),
			'date': forms.HiddenInput(),
			'shift_start_time': forms.HiddenInput(),
			'shift_end_time': forms.HiddenInput(),
			'status':forms.HiddenInput(),
		#The below lines were commented because they are not required in this single page.
		}