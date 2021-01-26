from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		widgets = {
			'username': TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'}),
			'email': TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}),
			'password1': PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}),
			'password2': PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Confirm Password'}),
		}


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'
