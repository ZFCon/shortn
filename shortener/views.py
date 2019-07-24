from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from shortener.models import ShortnURL

# Create your views here.
class home(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Your URL is ' + get_object_or_404(ShortnURL, short_code = kwargs['SC']).url)