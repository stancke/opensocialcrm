from campanhas.models import Campanha
from django.contrib import admin
from redes_sociais.models import Twitter as Config_twitter
from api.api import Twitter, Facebook

def publicar(modeladmin, request, queryset):
    
    
    for rede in redes:
        if rede == 'Twitter':
            configs = Config_twitter.objects.all()
            a = Twitter(configs)
            a.enviaTweet(desc)
    
    queryset.update(status='P')


class CampanhaAdmin(admin.ModelAdmin):
    
    list_display = ('redes_sociais','titulo','descricao','criada_em', 'status')
    search_fields = ['titulo', 'descricao']
    
    fieldsets = (
        (None, {
            'fields': ('redes_sociais','titulo', 'descricao')
        }),
    )

    actions = [publicar]
    
admin.site.register(Campanha, CampanhaAdmin)

