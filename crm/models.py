from django.db import models

class Lead(models.Model):
   
    nome = models.CharField(max_length=20)
    telefone = models.PositiveIntegerField(max_length=20, null=True, blank=True)
    e_mail = models.EmailField(max_length=25, blank=True)
    twitter = models.CharField(max_length=20, blank=True)
    facebook = models.CharField(max_length=25, blank=True)
    linkedin = models.CharField(max_length=25, blank=True)
    
    def __unicode__(self):
        return self.nome
 
class Relacionamento(models.Model):
    
    REDES = (
        ('T', 'Twitter'),
        ('F', 'Facebook'),
        ('L', 'Linkedin'),
        ('E', 'Email')
    )
    
    lead = models.ForeignKey(Lead)
    contato = models.CharField(max_length=1, choices= REDES)    
    data_de_relacionamento = models.DateTimeField(auto_now_add=True, null=True)
    assunto = models.CharField(max_length=30)
    mensagem = models.TextField(max_length=150)
    enviado = models.BooleanField()
    
    def __unicode__(self):
        return self.lead.nome