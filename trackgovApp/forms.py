from django import forms
from django.forms import ModelForm
from .models import UserRegistration

class UserRegistrationForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)
    class Meta:
        model = UserRegistration
        fields = ['useremail', 'username', 'password', 'datereg']


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)
    

CATEGORIES_CHOICES = [
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
    ('indigenous', 'Indigenous'),
    ('jobs_wages', 'Jobs/Wages'),
    # ('context', 'Context'),
    ('law_enforcement', 'Law Enforcement'),
    ('lgbtq', 'LGBTQ+'),
    ('media_journalism', 'Media And Journalism'),
    ('millitary', 'Millitary'),
    ('public_office', 'Public Office'),
    ('privacy', 'Privacy'),
    ('religion', 'Religion'),
    ('social_programs', 'Social Programs'),
    ('taxes', 'Taxes'),
    ('technology', 'Technology'),
]


class CategoriesForm(forms.Form):
    categories = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=CATEGORIES_CHOICES)
    lat = forms.CharField()
    lng = forms.CharField()


