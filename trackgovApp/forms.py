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
    


CATEGORIES_CHOICES = [
    ('agriculture', 'Agriculture'),
    ('business', 'Business'),
    ('civil_rights', 'Civil Rights'),
    ('drug_policy', 'Drug Policy'),
    ('economy', 'Economy'),
    ('education', 'Education'),
    ('environment', 'Environment'),
    ('food_water', 'Food/Water'),
    ('foreign_policy', 'Foreign Policy'),
    ('guns', 'Guns'),
    ('healthcare', 'Healthcare'),
    ('immigration', 'Immigration'),
    ('jobs_wages', 'Jobs/Wages'),
    ('sports', 'Sports'),
    ('law_enforcement', 'Law Enforcement'),
    ('transportation', 'Transportation'),
    ('millitary', 'Millitary'),
    ('public_office', 'Public Office'),
    ('religion', 'Religion'),
    ('social_programs', 'Social Programs'),
    ('taxes', 'Taxes'),
    ('technology', 'Technology'),
]


class CategoriesForm(forms.Form):
    # agriculture = forms.CheckboxInput()
    # business = forms.CheckboxInput()
    # civil_rights = forms.CheckboxInput()
    # drug_policy = forms.CheckboxInput()
    # economy = forms.CheckboxInput()
    # education = forms.CheckboxInput()
    # environment = forms.CheckboxInput()
    # food_water = forms.CheckboxInput()
    # foreign_policy = forms.CheckboxInput()
    # guns = forms.CheckboxInput()
    # healthcare = forms.CheckboxInput()
    # immigration = forms.CheckboxInput()
    # jobs_wages = forms.CheckboxInput()
    # sports = forms.CheckboxInput()
    # law_enforcement = forms.CheckboxInput()
    # transportation = forms.CheckboxInput()
    # millitary = forms.CheckboxInput()
    # public_office = forms.CheckboxInput()
    # religion = forms.CheckboxInput()
    # social_programs = forms.CheckboxInput()

    # taxes = forms.CheckboxInput()
    # technology = forms.CheckboxInput()
    categories = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=CATEGORIES_CHOICES)


