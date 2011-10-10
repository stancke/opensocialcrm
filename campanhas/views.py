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
        
        for re in result['analytics']['allTime']['referrers']:
          
            if (re['id'] == 'twitter.com') or (re['id'] == 't.co'):
                quantidade_twitter += int(re['count'])
                result['analytics']['allTime']['referrers'][aux]['count'] = 0

            elif re['id'] == 'Unknown/empty':
            
                result['analytics']['allTime']['referrers'][aux]['id'] = 'Acesso Direto'
                
            elif re['id'] == 'www.facebook.com':
            
                result['analytics']['allTime']['referrers'][aux]['id'] = 'Facebook'

            aux = aux + 1
        
        objeto = {"count" : quantidade_twitter, "id": "Twitter"}
        
        result['analytics']['allTime']['referrers'].append(objeto)    

        return render_to_response('campanhas/resultados.html', {"campanha": camp, 
                                                                "result": result
                                                               }
                                  )
                                                
def autoriza_linkedin(request):
    
    return render_to_response('campanhas/linkedin.html', {
                                                          "url": request.REQUEST.get('url'),
                                                          "session": request.REQUEST.get('session')
                                                          }
                              )

def confirma_linkedin(request):
   
    from liclient import LinkedInAPI
    configs = Config_linkedin.objects.all()
    
    APIClient = LinkedInAPI(str(configs[0].linkedin_app_id), str(configs[0].linkedin_app_secret))
    
    access_token = APIClient.get_access_token(request.session['request_token'], request.REQUEST.get('codigo_confirmacao'))
    
    APIClient.set_status_update(access_token, request.session['campanha'].descricao)

    return HttpResponseRedirect('/sistema/painel/campanhas/campanha/')         
