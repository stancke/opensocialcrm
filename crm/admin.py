
from crm.models import Lead, Relacionamento
from django.contrib import admin


def Nome(obj):
    
    lead = Lead.objects.filter(id=obj.lead_id)
    return lead[0].nome

class LeadAdmin(admin.ModelAdmin):
    list_display = ('nome','e_mail','telefone','twitter','facebook','linkedin')
    search_fields = ['nome', 'e_mail', 'telefone']
    
class RelacionamentoAdmin(admin.ModelAdmin):
    list_display = (Nome,'contato','data', 'enviar')
    fieldsets = (
        (None, {
            'fields': ('lead','contato','data', 'mensagem','enviar')
        }),
    )
    search_fields = ['lead']

admin.site.register(Lead,LeadAdmin)
admin.site.register(Relacionamento, RelacionamentoAdmin)

