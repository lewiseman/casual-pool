from django.forms import ModelForm
from django import forms
from django.forms.widgets import DateInput, TimeInput
from educator.models import Educator
from .models import Attendance
from rostering.models import Shift



class StartShiftForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ['start_time']
        widgets = {
            'start_time': TimeInput(attrs={'type': 'time'}),
        }


class EndShiftForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ['end_time']
        widgets = {
            'end_time': TimeInput(attrs={'type': 'time'}),
        }