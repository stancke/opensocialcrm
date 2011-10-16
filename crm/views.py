from django.shortcuts import render_to_response
from django.http import HttpResponse
from api.api import Twitter, Facebook, Linkedin
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
        
        if request.REQUEST.get('rede_social') == 'twitter':
    
            a = Twitter()
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
                
            return render_to_response('crm/prospeccao_twitter.html', {
                                                     'mencoes':array_mencao,
                                                     'retweets':retweets
                                                     }
                                  )
        elif request.REQUEST.get('rede_social') == 'facebook':
                
            return render_to_response('crm/prospeccao_facebook.html', {
                                                     'dados':Facebook().getLeads(),
                                                     }
                                    )
        elif request.REQUEST.get('rede_social') == 'linkedin':
                    
            return render_to_response('crm/prospeccao_linkedin.html', {
                                                     'dados':Linkedin().getLeads(),
                                                     }
                                    )
                

   
@login_required   
def adicionar_lead(request):
    
    l = Lead(nome=request.REQUEST.get('nome'), 
             twitter=request.REQUEST.get('twitter'), 
             facebook=request.REQUEST.get('facebook'), 
             linkedin=request.REQUEST.get('linkedin')
             )
    l.save()

    return HttpResponse('{"adicionado": true}')