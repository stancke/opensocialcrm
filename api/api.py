import tweepy

class Twitter(object):
    
    def __init__(self, twitter): 
          
        self.twitter = twitter

    
    def enviaTweet(self, descricao):

        for config in self.twitter:
            
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
            api.update_status(descricao)
        
    def getRetweets(self):
        
        api = tweepy.API(self.auth)
        return api.retweets_of_me()
    
    def getBusca(self, termo):
        
        for config in self.twitter:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_key, config.access_secret)
            api = tweepy.API(auth)
        
        return api.search(termo)
        
class Facebook(object):
    
    FACEBOOK_API_KEY = ''
    FACEBOOK_APP_ID = '205578726165733'
    FACEBOOK_APP_SECRET = '75f2b8ef906d1a3cc99beec92c65430c'
    
    #def __init__(self, request):

        
    #def enviaMensagem(self, mensagem):
        

        
class Linkedin(object):
    
    def __init__(self):
        print "sas"