from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from campanhas.models import Campanha
from redes_sociais.models import Twitter as Config_twitter
from api.api import Twitter, Facebook

def index(request,url):

    if request.user.is_authenticated():
        
        if request.method == 'GET':
            try:
                camp = Campanha.objects.filter(id=url)
            except:
                camp = ''
            
        configs = Config_twitter.objects.all()
        t = Twitter(configs)
                
        r = t.getBusca("partiu")
        coisa = 0
        for aux in r:
            coisa = coisa + 1
            return HttpResponse(aux.text)
        return HttpResponse(coisa)
        return render_to_response('resultados/index.html', {"campanhas": camp})
    else:
        return HttpResponseRedirect("/erro_autenticacao/")
