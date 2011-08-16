from django.db import models
from djangotoolbox.fields import ListField

class RedesSociais(models.Model):
    
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
