from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from shortener.models import ShortnURL
from .forms import ShortnForms

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = ShortnForms()
        context = {'form': form}
        return render(request ,'shortener/home.html', context)
    def post(self, request, *args, **kwargs):
        form = ShortnForms(request.POST)
        context = {'form': form}
        template = 'shortener/home.html'
        if form.is_valid():
            new_url = form.cleaned_data['url']
            if 'http' not in new_url:
                new_url = 'http://' + str(new_url)
            obj, created = ShortnURL.objects.get_or_create(url = new_url)
            if created:
                template = 'shortener/success.html'
                context['shortcode'] = get_short_code
                context['url'] = new_url
                pass
            else:
                context['url'] = new_url
                context['shortcode'] = obj.get_short_code
                template = 'shortener/exists.html'
                pass
        return render(request, template, context)            
class URL_Redirect(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(get_object_or_404(ShortnURL, short_code = kwargs['SC']).url)