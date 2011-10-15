from crm.models import Lead, Relacionamento
from api.api import Twitter
from django.contrib import admin
from redes_sociais.models import Twitter as Config_twitter, Facebook as Config_facebook, Linkedin as Config_linkedin
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
    #try:
    
    if rel.contato == 'T':

        configs = Config_twitter.objects.all()
        t = Twitter(configs)
        t.criarAmigo(lead.twitter)
        t.enviaTweet("@"+lead.twitter + ": " + rel.mensagem)
        
    elif rel.contato == 'F':
        import urllib
        import urllib2
        import json
        configs = Config_facebook.objects.all()
        values = {"access_token" : configs[0].access_token,
                  "message": rel.mensagem
                 }
        gurl = 'https://graph.facebook.com/%s/feed' % (lead.facebook)
        
        data = urllib.urlencode(values)
        req = urllib2.Request(gurl, data)
        req.add_header('User-Agent', 'toolbar')
        results = json.load(urllib2.urlopen(req))
    
    elif rel.contato == 'L':
        from liclient import LinkedInAPI
        configs = Config_linkedin.objects.all()
        
        APIClient = LinkedInAPI(str(configs[0].linkedin_app_id), str(configs[0].linkedin_app_secret))
        token = {'oauth_token_secret': str(configs[0].oauth_token_secret),'oauth_token': str(configs[0].access_token)}
        rec = []
        rec.append(lead.linkedin)
        APIClient.send_message(token, rec, rel.assunto , rel.mensagem)
    
    elif rel.contato == 'E':
        from django.core.mail import send_mail

        send_mail(rel.assunto, rel.mensagem, 'from@opensocialcrm.com',
                  [lead.e_mail], fail_silently=False)
        
    #except:
    #    enviado = False
        
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
