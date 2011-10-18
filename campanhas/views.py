from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from campanhas.models import Campanha
from redes_sociais.models import Twitter as Config_twitter, Linkedin as Config_linkedin
from api.api import Twitter
from api.google import Google

@login_required
def index(request):

    camp = Campanha.objects.filter(status=True).order_by('-criada_em')
    qtd = Campanha.objects.filter(status=True).count()
    
    return render_to_response('campanhas/index.html', {
                                                            'campanhas': camp,
							    'qtd':qtd,
							}
				 )
    

@login_required
def resultados(request):

    if request.method == 'POST' or request.method == 'GET':
            
        string = request.REQUEST
        id_campanha = string.get('campanha')
        camp = Campanha.objects.get(pk=id_campanha)
            
        result = Google().analisar_dados(camp.url_reduzida)
        aux = 0
        quantidade_twitter = 0
        quantidade_twitter_mes = 0
        quantidade_twitter_dia = 0
        quantidade_twitter_hora = 0
        
        try:
            for re in result['analytics']['allTime']['referrers']:
              
                if (re['id'] == 'twitter.com') or (re['id'] == 't.co'):
                    quantidade_twitter += int(re['count'])
                    result['analytics']['allTime']['referrers'][aux]['count'] = 0
    
                elif re['id'] == 'Unknown/empty':
                
                    result['analytics']['allTime']['referrers'][aux]['id'] = 'Acesso Direto'
                    
                elif re['id'] == 'www.facebook.com':
                
                    result['analytics']['allTime']['referrers'][aux]['id'] = 'Facebook'
                
                elif re['id'] == 'www.linkedin.com':
                
                    result['analytics']['allTime']['referrers'][aux]['id'] = 'LinkedIn'
    
                aux = aux + 1
                
            aux = 0
            for re in result['analytics']['month']['referrers']:
              
                if (re['id'] == 'twitter.com') or (re['id'] == 't.co'):
                    quantidade_twitter_mes += int(re['count'])
                    result['analytics']['month']['referrers'][aux]['count'] = 0
    
                elif re['id'] == 'Unknown/empty':
                
                    result['analytics']['month']['referrers'][aux]['id'] = 'Acesso Direto'
                    
                elif re['id'] == 'www.facebook.com':
                
                    result['analytics']['month']['referrers'][aux]['id'] = 'Facebook'
                
                elif re['id'] == 'www.linkedin.com':
                
                    result['analytics']['month']['referrers'][aux]['id'] = 'LinkedIn'
    
                aux = aux + 1
            
            aux = 0
            for re in result['analytics']['day']['referrers']:
              
                if (re['id'] == 'twitter.com') or (re['id'] == 't.co'):
                    quantidade_twitter_dia += int(re['count'])
                    result['analytics']['day']['referrers'][aux]['count'] = 0
    
                elif re['id'] == 'Unknown/empty':
                
                    result['analytics']['day']['referrers'][aux]['id'] = 'Acesso Direto'
                    
                elif re['id'] == 'www.facebook.com':
                
                    result['analytics']['day']['referrers'][aux]['id'] = 'Facebook'
                
                elif re['id'] == 'www.linkedin.com':
                
                    result['analytics']['day']['referrers'][aux]['id'] = 'LinkedIn'
    
                aux = aux + 1
                
            aux = 0
            for re in result['analytics']['twoHours']['referrers']:
              
                if (re['id'] == 'twitter.com') or (re['id'] == 't.co'):
                    quantidade_twitter_hora += int(re['count'])
                    result['analytics']['twoHours']['referrers'][aux]['count'] = 0
    
                elif re['id'] == 'Unknown/empty':
                
                    result['analytics']['twoHours']['referrers'][aux]['id'] = 'Acesso Direto'
                    
                elif re['id'] == 'www.facebook.com':
                
                    result['analytics']['twoHours']['referrers'][aux]['id'] = 'Facebook'
                
                elif re['id'] == 'www.linkedin.com':
                
                    result['analytics']['twoHours']['referrers'][aux]['id'] = 'LinkedIn'
    
                aux = aux + 1
        except:
            erro = 1
        try:
            objeto = {"count" : quantidade_twitter, "id": "Twitter"}
            result['analytics']['allTime']['referrers'].append(objeto)
            
            objeto = {"count" : quantidade_twitter_mes, "id": "Twitter"}
            result['analytics']['month']['referrers'].append(objeto)  
            
            objeto = {"count" : quantidade_twitter_dia, "id": "Twitter"}
            result['analytics']['day']['referrers'].append(objeto)   
            
            objeto = {"count" : quantidade_twitter_hora, "id": "Twitter"}
            result['analytics']['twoHours']['referrers'].append(objeto)
        
        except:
            erro =1

        return render_to_response('campanhas/resultados.html', { 
                                                                "result": result
                                                               }
                                  )
