
from crm.models import Lead, Relacionamento
from django.contrib import admin

class LeadAdmin(admin.ModelAdmin):
    list_display = ('nome','e_mail','telefone','twitter','facebook','linkedin')
    search_fields = ['nome', 'e_mail', 'telefone']
    
class RelacionamentoAdmin(admin.ModelAdmin):
    list_display = ('lead','contato','data')
    search_fields = ['lead']

admin.site.register(Lead,LeadAdmin)
admin.site.register(Relacionamento, RelacionamentoAdmin)

