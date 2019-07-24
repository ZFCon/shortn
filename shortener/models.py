from django.db import models
from .utils import create_code

# Create your models here.
class ShortnURL(models.Model):
    url = models.CharField(max_length = 220 )
    short_code = models.CharField(max_length = 15, unique=True, blank = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default = True)
    def __str__(self):
        return str(self.url)
    
    def save(self, *args, **kwargs):
        self.short_code = create_code(self)
        super(ShortnURL, self).save(*args, **kwargs)