from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from shortener.models import ShortnURL
from .forms import ShortnForms

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = ShortnForms(request.POST)
        context = {'form': form}
        return render(request ,'shortener/home.html', context)
    def post(self, request, *args, **kwargs):
        form = ShortnForms(request.POST)
        context = {'form': form}
        return render(request ,'shortener/home.html', context)
class URL_Redirect(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(get_object_or_404(ShortnURL, short_code = kwargs['SC']).url)