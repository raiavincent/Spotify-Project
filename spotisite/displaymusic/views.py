from django.http import HttpResponse
from .models import Song

def index(request):
    return HttpResponse("Hello, world. This is where the displays will live.")

def index(request):
    latest_song_list = Song.objects.order_by('-pub_date')[:5]
    template = loader.get_template('displaymusic/index.html')
    context = {
        'latest_song_list': latest_song_list,
    }
    return HttpResponse(template.render(context, request))