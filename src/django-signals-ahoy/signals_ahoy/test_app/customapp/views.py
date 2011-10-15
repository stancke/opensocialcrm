from django.shortcuts import render_to_response
from django.template import RequestContext
import signals
from models import Note
from datetime import datetime
    
def collect_urls(request):
    ctx = RequestContext(request, {})
    return render_to_response('customapp/index.html', ctx)

def async_note_create(request):
    ct1 = Note.objects.all().count()
    note =  datetime.now().ctime()
    signals.async_note.send(None, note=note)
    ct2 = Note.objects.all().count()
    latest = Note.objects.latest('id')
    ctx = RequestContext(request, {
        'startct': ct1,
        'endct' : ct2,
        'latest' : latest
    })
    return render_to_response('customapp/async_note.html', ctx)
