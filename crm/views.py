from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from campanhas.models import Campanha
from redes_sociais.models import Twitter as Config_twitter
from api.api import Twitter

def index(request):

    camp = Campanha.objects.filter(status=True)

    if request.user.is_authenticated():
        return render_to_response('crm/index.html')
    else:
        return HttpResponseRedirect("/erro_autenticacao/")