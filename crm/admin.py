from crm.models import Lead, Relacionamento
from django.contrib import admin

class RelacionamentoInline(admin.StackedInline):
    model = Relacionamento

class LeadAdmin(admin.ModelAdmin):
    list_display = ('nome','e_mail','telefone','twitter','facebook','linkedin')
    search_fields = ['nome', 'e_mail', 'telefone']
    
    inlines = [
        RelacionamentoInline,
    ]
    
def enviar_mesagem(self, request, queryset):

    queryset.update(enviar=True, )
    
class RelacionamentoAdmin(admin.ModelAdmin):
    list_display = ('lead','contato','data', 'enviar')
    fieldsets = (
        (None, {
            'fields': ('lead','contato','data', 'mensagem','enviar')
        }),
    )
    search_fields = ['lead']
    actions = [enviar_mesagem]

admin.site.register(Lead,LeadAdmin)
admin.site.register(Relacionamento, RelacionamentoAdmin)