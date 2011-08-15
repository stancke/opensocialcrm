from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):

    return render_to_response('campanhas/index.html')

def nova(request):

    return render_to_response('campanhas/nova.html')
