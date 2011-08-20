# -*- coding: utf-8 -*- 
from campanhas.models import Campanha
from django.contrib import admin
from redes_sociais.models import Twitter as Config_twitter
from api.api import Twitter, Facebook
import datetime

def publicar(modeladmin, request, queryset):
    
    '''
    for rede in redes:
        if rede == 'Twitter':
            configs = Config_twitter.objects.all()
            a = Twitter(configs)
            a.enviaTweet(desc)
    '''
    queryset.update(status=True, enviado_em=datetime.datetime.now())

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

