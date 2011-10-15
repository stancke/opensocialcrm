from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from redes_sociais.models import Twitter as Config_twitter, Facebook as Config_facebook, Linkedin as Config_linkedin
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
        
        if request.REQUEST.get('rede_social') == 'twitter':
    
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
                
            return render_to_response('crm/prospeccao_twitter.html', {
                                                     'mencoes':array_mencao,
                                                     'retweets':retweets
                                                     }
                                  )
        elif request.REQUEST.get('rede_social') == 'facebook':
            
            import urllib
            import urllib2
            import json
            configs = Config_facebook.objects.all()
            gurl = 'https://graph.facebook.com/me/feed?access_token=' + configs[0].access_token
            req = urllib2.Request(gurl)
            req.add_header('User-Agent', 'toolbar')
            results = json.load(urllib2.urlopen(req))

                
            return render_to_response('crm/prospeccao_facebook.html', {
                                                     'dados':results['data'],
                                                     }
                                    )
        elif request.REQUEST.get('rede_social') == 'linkedin':
             
            from liclient import LinkedInAPI
            configs = Config_linkedin.objects.all()
            
            APIClient = LinkedInAPI(str(configs[0].linkedin_app_id), str(configs[0].linkedin_app_secret))
            token = {'oauth_token_secret': str(configs[0].oauth_token_secret),'oauth_token': str(configs[0].access_token)}
            key = APIClient.get_network_updates(token, scope="self")
           
            chaves = []
            try:
                for a in key['results']:
                    chaves.append(a.update_key)
            except:
                erro =1
    
            resultado = []
            for chave in chaves:
                
                result = APIClient.get_comment_feed(token, chave)
                
                if result != 'LinkedInError':
                    resultado.append(result)
                    
            resultados_finais = []
            auxiliar = 0
            for aux in resultado:
                try:
                    for a in aux:
                        jsons = {}
                        jsons['titulo'] = a._NetworkUpdateComment__content.headline
                        jsons['update_content'] = a.update_content
                        jsons['first_name'] = a.first_name
                        jsons['last_name'] = a.last_name
                        jsons['profile_url'] = a._NetworkUpdateComment__content.profile_url
                        jsons['id'] = a._NetworkUpdateComment__content.id
                        contador = int(auxiliar)
                        jsons['campanha'] = key['results'][contador].update_content
                        resultados_finais.append(jsons)
                except:
                    erro = 12
                auxiliar = auxiliar +1
                    
            return render_to_response('crm/prospeccao_linkedin.html', {
                                                     'dados':resultados_finais,
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
