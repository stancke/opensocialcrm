from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from crm.models import Lead, Relacionamento
from campanhas.models import Campanha
from api.api import Twitter
from redes_sociais.models import Twitter as Config_twitter

def index(request):

    camp = Campanha.objects.filter(status=True)
    relacionamentos = Relacionamento.objects.all()[:5]
    leads = Lead.objects.all()[:5]
    
    configs = Config_twitter.objects.all()
    a = Twitter(configs)
    #mencoes = a.getMencoes()
    #ret = a.getRetweets()
    #HttpResponse(ret)
    
    if request.user.is_authenticated():
        return render_to_response('dashboard/index.html', {
                                                            'leads' : leads,
                                                            'relacionamentos' : relacionamentos,
                                                            'campanhas': camp
                                                           }
                                  )
    else:
        return HttpResponseRedirect("/erro_autenticacao/")