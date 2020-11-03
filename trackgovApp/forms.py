from django import forms
from django.forms import ModelForm

from .models import UserRegistration


class UserRegistrationForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)

    class Meta:
        model = UserRegistration
        fields = ['firstname', 'lastname', 'useremail', 'username', 'password', 'datereg']



class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)
    
