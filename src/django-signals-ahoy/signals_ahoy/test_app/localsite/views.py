from django.shortcuts import render_to_response
from django.template import RequestContext
from signals_ahoy import signals
import forms
import logging

log = logging.getLogger('views')

def example(request):
    ctx = RequestContext(request, {})
    return render_to_response('localsite/example.html', ctx)
    
def index(request):
    ctx = RequestContext(request, {})
    return render_to_response('localsite/index.html', ctx)


def search(request):
    """Perform a search based on keywords and categories in the form submission"""
    if request.method=="GET":
        data = request.GET
    else:
        data = request.POST

    keywords = data.get('keywords', '').split(' ')

    keywords = filter(None, keywords)

    results = {}

    signals.application_search.send(None, request=request, keywords=keywords, results=results)
    
    context = RequestContext(request, {
            'results': results,
            'keywords' : keywords})
    return render_to_response('localsite/search.html', context)

def signalled_view(request):
    ctx = {
        'data' : 'not modified'
    }
    
    signals.view_prerender.send('signalled_view', context=ctx)
    context = RequestContext(request, ctx)
    return render_to_response('localsite/signalled_view.html', context)

def form_example(request):
    data = {}
    if request.method == "POST":
        form = forms.ExampleForm(request.POST)
        if form.is_valid():
            log.debug('frm: %s', form.cleaned_data)
            data = form.save()
            log.debug('data: %s', data)
        else:
            log.debug('not valid: %s', form.errors)
    else:
        log.debug('fresh form')
        form = forms.ExampleForm()
        
    ctx = RequestContext(request, {
        'form' : form,
        'formdata' : data
    })
    return render_to_response('localsite/form_example.html', ctx)
