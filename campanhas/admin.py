# -*- coding: utf-8 -*- 
from campanhas.models import Campanha
from django.contrib import admin
from redes_sociais.models import Twitter as Config_twitter, Facebook as Config_facebook, Linkedin as Config_linkedin
from api.api import Twitter, Facebook
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from api.google import Google
import facebook

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
    titulo = ''
    mensagem = ''
    queryset.update(status=True, enviado_em=datetime.datetime.now())
    
    if camp.twitter == True:

        configs = Config_twitter.objects.all()
        a = Twitter(configs)
        try:
            a.enviaTweet(camp.descricao)
            titulo = camp.titulo
            mensagem = 'publicada com sucesso!'
        except:
            titulo = camp.titulo
            mensagem = 'obteve falha ao publicar!'
 
    if camp.facebook == True:
        
        import urllib
        import urllib2
        import json
        configs = Config_facebook.objects.all()
        gurl = 'https://graph.facebook.com/me/friends?access_token=' + configs[0].access_token
        req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'toolbar')
        results = json.load(urllib2.urlopen(req))
        
        return HttpResponse(results['data'])
        
        
    if camp.linkedin == True:
        
        from liclient import LinkedInAPI
        configs = Config_linkedin.objects.all()
        
        APIClient = LinkedInAPI(str(configs[0].linkedin_app_id), str(configs[0].linkedin_app_secret))
        tokens = {'oauth_token_secret': str(configs[0].oauth_token_secret),'oauth_token': str(configs[0].access_token)}
        APIClient.set_status_update(tokens, camp.descricao)
        
        
    self.message_user(request, "Campanha " + titulo + " " + mensagem )
            

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
