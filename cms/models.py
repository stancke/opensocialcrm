from django.db import models

class Configuracoes(models.Model):
   
    titulo = models.CharField(max_length=20)
    slogan = models.CharField(max_length=25)
    descricao_index = models.TextField(max_length=120)

