from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from campanhas.models import Campanha
from redes_sociais.models import Twitter as Config_twitter
from api.api import Twitter
from crm.models import Lead

def index(request):

    if request.user.is_authenticated():
        return render_to_response('crm/index.html')
    else:
        return HttpResponseRedirect("/erro_autenticacao/")

def prospeccao(request):

    camp = Campanha.objects.filter(status=True)
    
    configs = Config_twitter.objects.all()
    a = Twitter(configs)
    mencoes = a.getMencoes()
    retweets = a.getRetweets()
    
    #return HttpResponse(mencoes)
    #return HttpResponse({mencoes})

    if request.user.is_authenticated():
        return render_to_response('crm/prospeccao.html', {
                                                     'mencoes':mencoes,
                                                     'retweets':retweets
                                                     }
                                  )
    else:
        return HttpResponseRedirect("/erro_autenticacao/")
    
def adicionar_lead(request):
    
    string = request.REQUEST
    l = Lead(nome=string.get('nome'), twitter=string.get('twitter'))
    l.save()

    return HttpResponse('{"adicionado": true}')