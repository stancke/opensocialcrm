from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from redes_sociais.models import Twitter as Config_twitter
from api.api import Twitter
from crm.models import Lead
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    return render_to_response('crm/index.html')

@login_required
def prospeccao(request):
    
    erro = False
    array_mencao = None
    retweets = None
    
    if request.method == 'GET':
            
        string = request.REQUEST
        twitter = string.get('twitter')
        
        if twitter == 'on':
    
            configs = Config_twitter.objects.all()
            a = Twitter(configs)
            mencoes = a.getMencoes()
            retweets = a.getRetweets()
        
            aux = 0
            
            array_mencao = []
            
            for mencao in mencoes:
                array_mencao.append(mencao)
            
            for mencao in a.getMencoes():
                
                qtd = Lead.objects.filter(twitter = mencao.user.screen_name).count()
                
                if qtd > 0:
        
                    array_mencao[aux].user.adicionado = "True"
                else:
                    array_mencao[aux].user.adicionado = "False"
                        
                aux = aux + 1
                
        else:
            erro = True

    return render_to_response('crm/prospeccao.html', {
                                                     'mencoes':array_mencao,
                                                     'retweets':retweets
                                                     }
                                  )
@login_required   
def adicionar_lead(request):
    
    string = request.REQUEST
    l = Lead(nome=string.get('nome'), twitter=string.get('twitter'))
    l.save()

    return HttpResponse('{"adicionado": true}')
