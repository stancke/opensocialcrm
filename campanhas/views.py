from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from campanhas.models import Campanha
from redes_sociais.models import Twitter as Config_twitter
from api.api import Twitter
from api.google import Google
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    camp = Campanha.objects.filter(status=True)
    qtd = Campanha.objects.filter(status=True).count()
    
    return render_to_response('campanhas/index.html', {
                                                            'campanhas': camp,
							    'qtd':qtd,
							}
				 )
    

@login_required
def resultados(request):

    if request.method == 'POST':
            
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
                                                                 
