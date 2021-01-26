from django.forms import ModelForm
from .models import Availability
from django import forms
from django.forms.widgets import DateInput, TimeInput


class AvailabilityForm(ModelForm):
	class Meta:
		model = Availability
		fields = '__all__'
		exclude = ['date_created']
		widgets = {
            'educator':forms.HiddenInput(),
			# 'date': DateInput(attrs={'class': 'form-control date-picker', 'placeholder' : 'Select Date'}),
			# 'start_time': TimeInput(attrs={'class': 'form-control time-picker', 'placeholder' : 'Select time'}),
			# 'end_time': TimeInput(attrs={'class': 'form-control time-picker', 'placeholder' : 'Select time'}),
            'date': DateInput(attrs={'type': 'date'}),
			'start_time': TimeInput(attrs={'type': 'time'}),
			'end_time': TimeInput(attrs={'type': 'time'}),
        }