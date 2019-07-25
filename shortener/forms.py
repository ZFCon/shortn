from django import forms
from django.core.validators import URLValidator
from .validator import clean_url

class ShortnForms(forms.Form):
    error_css_class = 'error'
    url = forms.CharField(label = '', validators = [clean_url], widget = forms.TextInput(
        attrs ={
            'class': "form-control",
            'type': "text",
            'placeholder': "Search",
            'aria-label': "Search"
        }
    ))