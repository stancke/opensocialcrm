# -*- coding: utf-8 -*- 
import tweepy
import facebook
from django.http import HttpResponse


class Twitter(object):
    
    def __init__(self, twitter): 
          
        self.twitter = twitter
        
        
    
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
        
        
class Facebook(object):
    
    def __init__(self, facebook): 
        self.facebook = facebook
    
    
    def postaMensagem(self, mensagem):

        from facebook import Facebook
        
        for config in self.facebook:
            facebook = Facebook(config.facebook_app_id, config.facebook_app_secret)
            coisa = facebook.auth.createToken()
            graph = facebook.auth.getSession()
            graph.put_object("me", "feed", message=mensagem)
	
	#facebook = Facebook('205578726165733', '75f2b8ef906d1a3cc99beec92c65430c')
        #coisa = facebook.auth.createToken()

        
class Linkedin(object):
    
    def __init__(self):
        print "sas"
