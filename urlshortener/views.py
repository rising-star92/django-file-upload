from django.shortcuts import render
from .forms import ShortenerForm

# Create your views here.

def home_view(request):
    template = 'urlshortener/home.html'

    context = {}

    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url

            context['new_url'] = new_url
            context['long_url'] = long_url
            
            return render(request, template, context)
        
        context['errors'] = used_form.errors

        return render(request, template, context)