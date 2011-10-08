# -*- coding: utf-8 -*- 
from django.db import models
    
class Campanha(models.Model):
    
   
    criada_em = models.DateTimeField(auto_now_add=True, null=True)
    enviado_em = models.DateTimeField(null=True)
    twitter = models.BooleanField()
    facebook = models.BooleanField()
    linkedin = models.BooleanField()
    titulo = models.CharField(max_length=25)
    descricao = models.TextField(max_length=120)
    url = models.URLField(verify_exists=False, max_length=100)
    url_reduzida = models.URLField(verify_exists=False,max_length=100)
    status = models.BooleanField()
    
    def __unicode__(self):
        return self.titulo
