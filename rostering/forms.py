from django.forms import ModelForm
from django import forms
from django.forms.widgets import TimeInput
from rostering.models import Shift


class AddShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = '__all__'
        widgets ={
            'shift_start': TimeInput(attrs={'type': 'time'}),
            'shift_end': TimeInput(attrs={'type': 'time'}),
        }