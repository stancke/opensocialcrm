# -*- coding: utf-8 -*- 
import tweepy
import facebook
from django.http import HttpResponse
from redes_sociais.models import Twitter as Config_twitter, Facebook as Config_facebook, Linkedin as Config_linkedin
from crm.models import Lead


class Twitter(object):
    
    def __init__(self): 
        
        self.twitter = Config_twitter.objects.all()
        
    
    def enviaTweet(self, descricao):

        for config in self.twitter:
            
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            api.update_status(descricao)
            
    def criarAmigo(self, usuario):

        for config in self.twitter:
            
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            api.create_friendship(usuario)
            
    def enviaMensagemDireta(self, usuario, texto):

        for config in self.twitter:
            
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            api.send_direct_message(user=usuario, text=texto)

    def getRetweets(self, limite = None):
        
        for config in self.twitter:
            
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            return tweepy.Cursor(api.retweets_of_me).items(limite)
    
    def getBusca(self, termo):
        
        for config in self.twitter:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)

        return api.search(termo, rpp=25, lang='pt')
    
    def getMencoes(self, limite = None):
        
        for config in self.twitter:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            
            return tweepy.Cursor(api.mentions).items(limite)
          
    def getHomeTimeline(self, limite = None):
        
        for config in self.twitter:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            
            return tweepy.Cursor(api.user_timeline).items(limite)
        
    def getResultadoCampanha(self, campanha):
        pass
        
        
class Facebook(object):
    
    def enviaMensagem(self, mensagem):

        import urllib
        import urllib2
        import json
        configs = Config_facebook.objects.all()
        values = {"access_token" : configs[0].access_token,
                  "message": mensagem
                 }
        gurl = 'https://graph.facebook.com/me/feed'
        
        data = urllib.urlencode(values)
        req = urllib2.Request(gurl, data)
        req.add_header('User-Agent', 'toolbar')
        results = json.load(urllib2.urlopen(req))
        
    def enviaMensagemDireta(self, lead, mensagem):
        import urllib
        import urllib2
        import json
        configs = Config_facebook.objects.all()
        values = {"access_token" : configs[0].access_token,
                  "message": mensagem
                 }
        gurl = 'https://graph.facebook.com/%s/feed' % (lead)
        
        data = urllib.urlencode(values)
        req = urllib2.Request(gurl, data)
        req.add_header('User-Agent', 'toolbar')
        results = json.load(urllib2.urlopen(req))
        
    def getLeads(self):
        import urllib
        import urllib2
        import json
        configs = Config_facebook.objects.all()
        gurl = 'https://graph.facebook.com/me/feed?access_token=' + configs[0].access_token
        req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'toolbar')
        
        retorno = json.load(urllib2.urlopen(req))
        retorno2 = retorno
        dados_comments_final =  []
        dados_likes_final =  []
        for dado in retorno['data']:
             
            try:
                
                for aux in dado['comments']['data']:
                    
                    dados_comment = {}
                    dados_comment['name'] = aux['from']['name']
                    dados_comment['id'] = aux['from']['id']
                    dados_comment['message'] = aux['message']
                    dados_comment['campanha'] = dado['message']
                    
                    if Lead.objects.filter(facebook = int(aux['from']['id'])).count() > 0:
                        dados_comment['lead'] = "True"
                    else:
                        dados_comment['lead'] = "False"
                    
                    dados_comments_final.append(dados_comment)

            except:
                erro = 1
                
        for dado in retorno2['data']:
             
            try:
                
                for aux_like in dado['likes']['data']:
                    
                    dados_likes = {}
                    dados_likes['name'] = aux_like['name']
                    dados_likes['id'] = aux_like['id']
                    dados_likes['campanha'] = dado['message']
                    
                    if Lead.objects.filter(facebook = int(aux_like['id'])).count() > 0:
                        dados_likes['lead'] = "True"
                    else:
                        dados_likes['lead'] = "False"
                    
                    dados_likes_final.append(dados_likes)
  

            except:
                erro = 1
                
                
                
        dados_tratados = {"dados_comments": dados_comments_final, "dados_likes":dados_likes_final}
        return dados_tratados
    
    def getResultadoCampanha(self, campanha):
        import urllib
        import urllib2
        import json
        configs = Config_facebook.objects.all()
        gurl = 'https://graph.facebook.com/me/feed?access_token=' + configs[0].access_token
        req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'toolbar')
        
        retorno = json.load(urllib2.urlopen(req))
        retorno2 = retorno
        
        qtd_comentarios = 0
        qtd_likes = 0
        
        for dado in retorno['data']:
             
            try:
                
                for aux in dado['comments']['data']:
                    
                    if(str(dado['message']) == campanha):
                        qtd_comentarios = qtd_comentarios + 1
            except:
                erro = 1
                
        for dado in retorno2['data']:
             
            try:
                
                for aux_like in dado['likes']['data']:
                    
                    if(dado['message'] == campanha):
                    
                        qtd_likes = qtd_likes +1

            except:
                erro = 1
                
        dados_tratados = {"qtd_comentarios": qtd_comentarios, "qtd_likes":qtd_likes}
        return dados_tratados
        
class Linkedin(object):
    
    def enviaMensagem(self, mensagem):
        
        from liclient import LinkedInAPI
        configs = Config_linkedin.objects.all()
        
        APIClient = LinkedInAPI(str(configs[0].linkedin_app_id), str(configs[0].linkedin_app_secret))
        tokens = {'oauth_token_secret': str(configs[0].oauth_token_secret),'oauth_token': str(configs[0].access_token)}
        
        APIClient.set_status_update(tokens, mensagem)
        
    def enviaMensagemDireta(self,lead, assunto, mensagem):
        from liclient import LinkedInAPI
        configs = Config_linkedin.objects.all()
        
        APIClient = LinkedInAPI(str(configs[0].linkedin_app_id), str(configs[0].linkedin_app_secret))
        token = {'oauth_token_secret': str(configs[0].oauth_token_secret),'oauth_token': str(configs[0].access_token)}
        rec = []
        rec.append(lead)
        APIClient.send_message(token, rec, assunto , mensagem)
        
    def getLeads(self):
        
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
                    
                    if Lead.objects.filter(linkedin = a._NetworkUpdateComment__content.id).count() > 0:
                        jsons['lead'] = "True"
                    else:
                        jsons['lead'] = "False"
                        
                    resultados_finais.append(jsons)
            except:
                erro = 12
            auxiliar = auxiliar +1
            
        return resultados_finais

    def getResultadoCampanha(self, campanha):
        
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
                
        quantidade_comentarios = 0
        contador = 0 
        auxiliar = 0
        
        for aux in resultado:
            try:
                for a in aux:
                    jsons = {}
                    
                    if (campanha == key['results'][contador].update_content):
                                                                             
                        contador = int(auxiliar)
                        jsons['campanha'] = key['results'][contador].update_content
                        quantidade_comentarios = quantidade_comentarios + 1
            
            except:
                erro = 12
            auxiliar = auxiliar +1
            
        return quantidade_comentarios