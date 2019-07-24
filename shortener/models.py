from django.db import models
import random,string

# Create your models here.

def generator(num = 6, char = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for _ in range(num))

class ShortnURL(models.Model):
    url = models.CharField(max_length = 220 )
    short_code = models.CharField(max_length = 15, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.url)
    
    def save(self, *args, **kwargs):
        self.short_code = generator()
        super(ShortnURL, self).save(*args, **kwargs)