from django.db import models

class Twitter(models.Model):
    
    
    usuario = models.CharField(max_length = 20)
    consumer_key = models.CharField(max_length = 100)
    consumer_secret = models.CharField(max_length = 100)
    access_key = models.CharField(max_length = 150)
    access_secret = models.CharField(max_length = 150)
    
    
class Facebook(models.Model):
    
    usuario = models.CharField(max_length = 20)
    facebook_app_id = models.CharField(max_length = 100)
    facebook_app_secret = models.CharField(max_length = 150)
    access_token= models.CharField(max_length = 150, blank=True, null=True)

class Linkedin(models.Model):
    
    usuario = models.CharField(max_length = 20)
    linkedin_app_id = models.CharField(max_length = 100)
    linkedin_app_secret = models.CharField(max_length = 100)
    access_token= models.CharField(max_length = 150, blank=True, null=True)
    oauth_token_secret = models.CharField(max_length = 150, blank=True, null=True)
