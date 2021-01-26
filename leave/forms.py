from django.forms import ModelForm
from django import forms
from django.forms.widgets import DateInput, TimeInput
from .models import Leaves
from django.forms.widgets import DateInput, TimeInput, Select, TextInput

class AddLeaveEducatorForm(ModelForm):
    class Meta:
        model = Leaves
        fields = ['leave_type', 'date_from', 'date_to', 'description','educator']
        widgets ={
            'educator':forms.HiddenInput(), 
            'date_from': DateInput(attrs={'type': 'date'}),
            'date_to': DateInput(attrs={'type': 'date'}),
            'leave_type': Select(attrs={'class': 'custom-select col-12'}),
            'description': TextInput(attrs={'class': 'form-control'}),
        }


class UpdateLeaveEducatorForm(ModelForm):
    class Meta:
        model = Leaves
        fields = ['leave_type', 'date_from', 'date_to', 'description']
        widgets ={
            #'staff':forms.HiddenInput(), 
            'date_from': DateInput(attrs={'type': 'date'}),
            'date_to': DateInput(attrs={'type': 'date'}),
            'leave_type': Select(attrs={'class': 'custom-select col-12'}),
            'description': TextInput(attrs={'class': 'form-control'}),
        }

    
class UpdateLeaveManagerForm(ModelForm):
    class Meta:
        model = Leaves
        fields = '__all__'
        widgets ={
            'date_from': DateInput(attrs={'type': 'date'}),
            'date_to': DateInput(attrs={'type': 'date'}),
            'leave_status': Select(attrs={'class': 'custom-select col-12'}),
            'educator': Select(attrs={'class': 'custom-select col-12'}),
            'leave_type': Select(attrs={'class': 'custom-select col-12'}),
            'description': TextInput(attrs={'class': 'form-control'}),
        }