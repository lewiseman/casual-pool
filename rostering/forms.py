from django.forms import ModelForm
from django import forms
from django.forms.widgets import TimeInput, TextInput
from rostering.models import Shift
from django.forms import formset_factory


class AddShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = '__all__'
        widgets ={
            'shift_start': TimeInput(attrs={'type': 'time'}),
            'shift_end': TimeInput(attrs={'type': 'time'}),
            'educator_shift': TextInput()
        }