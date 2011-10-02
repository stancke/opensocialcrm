# -*- coding: utf-8 -*- 
from campanhas.models import Campanha
from django.contrib import admin
from redes_sociais.models import Twitter as Config_twitter, Facebook as Config_facebook
from api.api import Twitter, Facebook
from django.http import HttpResponse
import datetime
from api.google import Google

def publicar(self, request, queryset):
    string = request.REQUEST
    camp = Campanha.objects.get(id=string.get('_selected_action'))
    camp.url_reduzida = Google().encurtaUrl(camp.url)
    camp.save()
    
    titulo = ''
    mensagem = ''
    if camp.twitter == True:

        configs = Config_twitter.objects.all()
        a = Twitter(configs)
        try:
            a.enviaTweet(camp.descricao + " " + camp.url_reduzida)
            queryset.update(status=True, enviado_em=datetime.datetime.now())
            titulo = camp.titulo
            mensagem = 'publicada com sucesso!'
        except:
            titulo = camp.titulo
            mensagem = 'obteve falha ao publicar!'
 
    if camp.facebook == True:
        
        configs = Config_facebook.objects.all()
        f = Facebook(configs)
        f.postaMensagem(camp.descricao + " " + camp.url_reduzida)
        
    self.message_user(request, "Campanha " + titulo + " " + mensagem )
            

class CampanhaAdmin(admin.ModelAdmin):    
    
    list_display = ('titulo','descricao','url','twitter','facebook', 'linkedin','criada_em','enviado_em', 'status')
    search_fields = ['titulo', 'descricao']
    
    fieldsets = (
        (None, {
            'fields': ('twitter','facebook', 'linkedin','titulo', 'descricao', 'url')
        }),
    )

    actions = [publicar]
    
admin.site.register(Campanha, CampanhaAdmin)
