from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def clean_url(value):
    urlv = URLValidator()
    try:
        if 'http://' or 'https://' not in value:
            value = 'http://' + str(value)
            urlv(value)
        elif 'http://' or 'https://' in value:
            urlv(value)
    except:
        raise ValidationError('Use a real URL')
    return value