from django.shortcuts import redirect
from urlshortener.models import Shortener
from django.http import HttpResponseRedirect, Http404

def index_redirect(request):
    return redirect('/file')

def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)
    except:
        raise Http404('Sorry this link is borken :(')