
from django.db import models
from djangotoolbox.fields import ListField

class Campanha(models.Model):
    
   
    criada_em = models.DateTimeField(auto_now_add=True, null=True)
    
    REDES = (
        ('T', 'Twitter'),
        ('F', 'Facebook'),
        ('L', 'Linkedin'),
    )
    
    redes_sociais = models.CharField(max_length=3, choices=REDES)
    titulo = models.CharField(max_length=25)
    descricao = models.TextField(max_length=120)
    url = models.CharField(max_length=25)
    STATUS = (
        ('P', 'Publicado'),
        ('N', 'Nao Publicado'),
    )
    status = models.CharField(max_length=1, choices=STATUS, default='N')