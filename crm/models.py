# -*- coding: utf-8 -*- 
from django.db import models

class Lead(models.Model):
   
    nome = models.CharField(max_length=30, help_text='Nome do Lead de no máximo 30 caracteres.')
    telefone = models.PositiveIntegerField(max_length=20, null=True, blank=True, help_text='Telefone do Lead de no máximo 30 caracteres.')
    e_mail = models.EmailField(max_length=25, blank=True, help_text='E-mail do Lead de no máximo 25 caracteres.')
    twitter = models.CharField(max_length=20, blank=True, help_text='Nome do Lead no Twitter, exemplo: \'OpenSocialCRM\'.')
    facebook = models.CharField(max_length=25, blank=True, help_text='ID do Lead no Facebook, exemplo: \'100003007922649\'.')
    linkedin = models.CharField(max_length=25, blank=True, help_text='ID do Lead no LinkedIn, exemplo: \'a2amgZ1wg3\'.')
    
    def __unicode__(self):
        return self.nome
 
class Relacionamento(models.Model):
    
    REDES = (
        ('T', 'Twitter'),
        ('F', 'Facebook'),
        ('L', 'Linkedin'),
        ('E', 'Email')
    )
    
    lead = models.ForeignKey(Lead, help_text='Selecione um Lead previamente cadastrado ou insira um novo.')
    contato = models.CharField(max_length=1, help_text='Canal em que será realizada a comunicação.', choices= REDES)    
    data_de_relacionamento = models.DateTimeField(auto_now_add=True, null=True)
    assunto = models.CharField(max_length=30, help_text='Será utilizado para o assunto do e-mail e para o assunto da mensagem do LinkedIn.')
    mensagem = models.TextField(max_length=150, help_text='Mensagem que será enviada para o Lead.')
    enviado = models.BooleanField()
    
    def __unicode__(self):
        return self.lead.nome