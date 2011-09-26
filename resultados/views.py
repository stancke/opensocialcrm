from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from campanhas.models import Campanha
from redes_sociais.models import Twitter as Config_twitter
from api.api import Twitter
from api.google import Google

def index(request):

    result = None
    dados_totais = None
    dados_dia = None
    dados_mes = None
    dados_horas  = None
    if request.user.is_authenticated():
        
        if request.method == 'POST':
            
            string = request.REQUEST
            id_campanha = string.get('campanha')
            camp = Campanha.objects.get(pk=id_campanha)
            
            result = Google().analisar_dados(camp.url_reduzida)

        try:
            dados_totais = {'total': result['analytics']['allTime']['shortUrlClicks'],
                     'locais' : result['analytics']['allTime']['referrers'],
                     'paises': result['analytics']['allTime']['countries'],
                     'browsers': result['analytics']['allTime']['browsers'],
                     'plataformas': result['analytics']['allTime']['platforms']
                    }
            
            dados_dia = {'total': result['analytics']['day']['shortUrlClicks'],
                     'locais' : result['analytics']['day']['referrers'],
                     'paises': result['analytics']['day']['countries'],
                     'browsers': result['analytics']['day']['browsers'],
                     'plataformas': result['analytics']['day']['platforms']
                    }
            
            dados_mes = {'total': result['analytics']['month']['shortUrlClicks'],
                     'locais' : result['analytics']['month']['referrers'],
                     'paises': result['analytics']['month']['countries'],
                     'browsers': result['analytics']['month']['browsers'],
                     'plataformas': result['analytics']['month']['platforms']
                    }
            
            dados_horas = {'total': result['analytics']['twoHours']['shortUrlClicks'],
                     'locais' : result['analytics']['twoHours']['referrers'],
                     'paises': result['analytics']['twoHours']['countries'],
                     'browsers': result['analytics']['twoHours']['browsers'],
                     'plataformas': result['analytics']['twoHours']['platforms']
                    }
            
            
        except:
            erro = ''
        
        
        
        
        #return HttpResponse(dados)
        #todos = result['analytics']['allTime']
        #mes = result['analytics']['month']
        
        #dados = {'todos' : todos}
        
        #return HttpResponse({dados})
            
        #configs = Config_twitter.objects.all()
        #t = Twitter(configs)
        '''        
        r = t.getBusca("partiu")
        coisa = 0
        for aux in r:
            coisa = coisa + 1
            return HttpResponse(aux.text)
        return HttpResponse(coisa)'''
        
        return render_to_response('resultados/index.html', {"campanha": camp, 
                                                                 "dados": dados_totais,
                                                                 "dados_dia": dados_dia,
                                                                 "dados_mes": dados_mes,
                                                                 "dados_horas":dados_horas
                                                                 }
                                  )
    else:
        return HttpResponseRedirect("/erro_autenticacao/")
    
    
