from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from crm.models import Lead, Relacionamento
from campanhas.models import Campanha
from api.api import Twitter
from redes_sociais.models import Twitter as Config_twitter

@login_required
def index(request):

    camp = Campanha.objects.filter(status=True)
    relacionamentos = Relacionamento.objects.all()[:5]
    leads = Lead.objects.all()[:5]
    timeline = None
    mencoes = None
    ret = None
    
    configs = Config_twitter.objects.all()
    a = Twitter(configs)
    timeline = a.getHomeTimeline(limite=3)
    mencoes = a.getMencoes(limite=3)
    ret = a.getRetweets(limite=3)
    
    return render_to_response('dashboard/index.html', {
                                                            'leads' : leads,
                                                            'relacionamentos' : relacionamentos,
                                                            'timeline': timeline,
                                                            'campanhas': camp,
                                                            'mencoes': mencoes,
                                                            'retweets': ret
                                                           }
                                  )
