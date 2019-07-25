from django import forms
from django.core.validators import URLValidator
from .validator import clean_url

class ShortnForms(forms.Form):
    url = forms.CharField(label = 'submet url', validators = [clean_url])