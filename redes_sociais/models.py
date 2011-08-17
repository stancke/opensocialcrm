from django.db import models
from djangotoolbox.fields import ListField

class Twitter(models.Model):
    
    
    usuario = models.CharField(max_length = 20)
    consumer_key = models.CharField(max_length = 100)
    consumer_secret = models.CharField(max_length = 100)
    access_key = models.CharField(max_length = 100)
    access_secret = models.CharField(max_length = 100)
    
    
class Facebook(models.Model):
    
    TIPO_REDE_SOCIAL = (
        ('T', 'Twitter'),
        ('F', 'Facebook'),
        ('L', 'LinkedIn'),
        ('G', 'Google+'),
    )
    rede_social = models.CharField(max_length=1, choices=TIPO_REDE_SOCIAL)
    usuario = models.CharField(max_length = 20)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length = 20)
