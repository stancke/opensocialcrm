# -*- coding: utf-8 -*- 
from django.db import models
from djangotoolbox.fields import ListField
    
class Campanha(models.Model):
    
   
    criada_em = models.DateTimeField(auto_now_add=True, null=True)
    enviado_em = models.DateTimeField(null=True)
    twitter = models.BooleanField()
    facebook = models.BooleanField()
    linkedin = models.BooleanField()
    titulo = models.CharField(max_length=25)
    descricao = models.TextField(max_length=120)
    status = models.BooleanField()