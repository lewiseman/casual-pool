from django.forms import ModelForm
from django import forms
from django.forms.widgets import DateInput, TimeInput, Select
from .models import Job

class JobForm(ModelForm):
	class Meta:
		model = Job
		fields = '__all__'
		exclude = ['date_created']
		widgets = {
			'manager':forms.HiddenInput(), 
			# 'date': DateInput(attrs={'class': 'form-control date-picker', 'placeholder' : 'Select Date'}),
			# 'shift_start_time': TimeInput(attrs={'class': 'form-control time-picker', 'placeholder' : 'Select time'}),
			# 'shift_end_time': TimeInput(attrs={'class': 'form-control time-picker', 'placeholder' : 'Select time'}),
			'date': DateInput(attrs={'type': 'date'}),
			'shift_start_time': TimeInput(attrs={'type': 'time'}),
			'shift_end_time': TimeInput(attrs={'type': 'time'}),
            'qualification': Select(attrs={'class': 'custom-select col-12'}),
		}	