# -*- coding: utf-8 -*- 
from campanhas.models import Campanha
from django.contrib import admin
from api.api import Twitter, Facebook, Linkedin
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from api.google import Google

def publicar(self, request, queryset):
    
    string = request.REQUEST
    camp = Campanha.objects.get(id=string.get('_selected_action'))
    request.session['campanha'] = camp
    '''
    import re
    m = re.search('http://.*\\s', camp.descricao)
    url_real = ''
    for l in list(m.group(0)):
        if l == ' ':
            break
        elif l != ' ':
            url_real += l

    url_reduzida = Google().encurtaUrl(url_real)
    
    camp.url = url_real
    camp.url_reduzida = url_reduzida
    camp.descricao = camp.descricao.replace(url_real, url_reduzida)
    camp.save()
    '''
    
    enviado = True
    
    try:
        if camp.twitter == True:
    
            Twitter().enviaTweet(camp.descricao)
     
        if camp.facebook == True:
            
            Facebook().enviaMensagem(camp.descricao)
            
        if camp.linkedin == True:
            
            Linkedin().enviaMensagem(camp.descricao)
    except:
        enviado = False
    
    if(enviado):
        queryset.update(status=True, enviado_em=datetime.datetime.now())    
        self.message_user(request, "Campanha enviada")
        
    else:
        self.message_user(request, "Erro em envio de campanha")
            

class CampanhaAdmin(admin.ModelAdmin):    
    
    list_display = ('titulo','descricao','twitter','facebook', 'linkedin','criada_em','enviado_em', 'status')
    search_fields = ['titulo', 'descricao']
    
    fieldsets = (
        (None, {
            'fields': ('twitter','facebook', 'linkedin','titulo', 'descricao')
        }),
    )

    actions = [publicar]
    
admin.site.register(Campanha, CampanhaAdmin)
