import tweepy

class Twitter(object):
    
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_KEY = ""
    ACCESS_SECRET = ""
    
    def __init__(self): 
          
        self.CONSUMER_KEY = 'e3gEGIOAml47NHEsgQyQvA'
        self.CONSUMER_SECRET = 'zeQAWpvF32GbvV4LbD3Mw8qYmiEtMUvW3h4fBXI9scY'
        self.ACCESS_KEY = '355529640-HHgSk0NqXUZO0UcXKgNUAPpoC0vTqZRKHh5zM9np'
        self.ACCESS_SECRET = 'HnWLmGp5gtp9CCL8HjiAIZfe9LLKKToRRZQYzRjwu0'
    
    def enviaTweet(self, descricao):

        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
        api = tweepy.API(auth)
        api.update_status(descricao)
        
        
class Facebook(object):
    
    def __init__(self):
        print "sas"
        
class Linkedin(object):
    
    def __init__(self):
        print "sas"