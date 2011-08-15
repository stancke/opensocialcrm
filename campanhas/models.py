from django.db import models
from djangotoolbox.fields import ListField

class Campanhas(models.Model):
   
    criada_em = models.DateTimeField(auto_now_add=True, null=True)
    redes_sociais = ListField()
    titulo = models.CharField(max_length=25)
    descricao = models.TextField(max_length=120)