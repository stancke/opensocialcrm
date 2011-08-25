from django.db import models

class Lead(models.Model):
   
    
    nome = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    e_mail = models.EmailField(max_length=25)
    twitter = models.CharField(max_length=20)
    facebook = models.CharField(max_length=25)
    linkedin = models.CharField(max_length=25)
 
class Relacionamento(models.Model):
    
    REDES = (
        ('T', 'Twitter'),
        ('F', 'Facebook'),
        ('L', 'Linkedin'),
    )
    
    lead = models.ForeignKey(Lead)
    contato = models.CharField(max_length=1, choices= REDES)    
    data = models.DateTimeField()
    mensagem = models.TextField(max_length=150)
    enviar = models.BooleanField()
    
    def __unicode__(self):
        return self.lead.nome


