# -*- coding: utf-8 -*- 
from django.db import models
    
class Campanha(models.Model):
    
   
    criada_em = models.DateTimeField(auto_now_add=True, null=True)
    enviado_em = models.DateTimeField(null=True)
    twitter = models.BooleanField(help_text='Esta opção atualiza a timeline no Twitter.')
    facebook = models.BooleanField(help_text='Esta opção altera o Feed no Facebook.')
    linkedin = models.BooleanField(help_text='Esta opção altera o status no LinkedIn.')
    titulo = models.CharField(max_length=25, help_text='Título usado somente para controle intern de no máximo 25 caracteres.')
    descricao = models.TextField(max_length=140, help_text='Descrição da campanha que será enviada para a rede social, máximo de 140 caracteres.')
    url = models.URLField(verify_exists=False, max_length=100, null=True, blank=True)
    url_reduzida = models.URLField(verify_exists=False,max_length=100)
    status = models.BooleanField()
    
    def __unicode__(self):
        return self.titulo
