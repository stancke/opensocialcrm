from crm.models import Lead, Relacionamento
from api.api import Twitter, Facebook, Linkedin
from django.contrib import admin
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
    lead = Lead.objects.get(pk = rel.lead.id)
    enviado = True
    
    try:
    
        if rel.contato == 'T':
            Twitter().enviaTweet("@"+lead.twitter + ": " + rel.mensagem)
            
        elif rel.contato == 'F':
            Facebook().enviaMensagemDireta(lead.facebook,rel.mensagem)
        
        elif rel.contato == 'L':
            Linkedin().enviaMensagemDireta(lead.linkedin, rel.assunto, rel.mensagem)
        
        elif rel.contato == 'E':
            from django.core.mail import send_mail
    
            send_mail(rel.assunto, rel.mensagem, request.user.email,
                      [lead.e_mail], fail_silently=False)
        
    except:
        enviado = False
        
    if enviado == True:
        queryset.update(enviado=True, )
    else:
        queryset.update(enviado=False, )
    
    
class RelacionamentoAdmin(admin.ModelAdmin):

    
    list_display = ('lead','contato','data_de_relacionamento', 'enviado')
    fieldsets = (
        (None, {
            'fields': ('lead','contato','assunto','mensagem')
        }),
    )
    search_fields = ['lead']
    actions = [enviar_mensagem]

admin.site.register(Lead,LeadAdmin)
admin.site.register(Relacionamento, RelacionamentoAdmin)
