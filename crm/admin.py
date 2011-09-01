from crm.models import Lead, Relacionamento
from api.api import Twitter
from django.contrib import admin
from redes_sociais.models import Twitter as Config_twitter
from django.http import HttpResponse

class RelacionamentoInline(admin.StackedInline):
    model = Relacionamento

class LeadAdmin(admin.ModelAdmin):
    list_display = ('nome','e_mail','telefone','twitter','facebook','linkedin')
    search_fields = ['nome', 'e_mail', 'telefone']
    
    inlines = [
        RelacionamentoInline,
    ]
    
def enviar_mensagem(self, request, queryset):

    string = request.REQUEST
    rel = Relacionamento.objects.get(id=string.get('_selected_action'))
    lead = Lead.objects.filter(id = rel.lead.id)
    
    enviado = True
        
    #try:
        
    if rel.contato == 'T':

        configs = Config_twitter.objects.all()
        t = Twitter(configs)
        #return HttpResponse(lead[0].twitter)
        t.enviaMensagemDireta('wstancke', rel.mensagem)
        
    #except:
    #    enviado = False
        
    if enviado == True:
        queryset.update(enviar=True, )
    else:
        queryset.update(enviar=False, )
    
    
class RelacionamentoAdmin(admin.ModelAdmin):
    list_display = ('lead','contato','data', 'enviar')
    fieldsets = (
        (None, {
            'fields': ('lead','contato','data', 'mensagem','enviar')
        }),
    )
    search_fields = ['lead']
    actions = [enviar_mensagem]

admin.site.register(Lead,LeadAdmin)
admin.site.register(Relacionamento, RelacionamentoAdmin)