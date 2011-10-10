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
        
        import oauth2 as oauth
        import urlparse

        consumer_key           = '205578726165733'
        consumer_secret        = '75f2b8ef906d1a3cc99beec92c65430c'
        
        graph = facebook.GraphAPI(acces_token=12)
        cookie = facebook.get_user_from_cookie(request.COOKIES, consumer_key,consumer_secret )
        return HttpResponse(cookie)
        graph = facebook.GraphAPI()
        
        configs = Config_facebook.objects.all()
        f = Facebook(configs)
        f.postaMensagem(camp.descricao)
        
    if camp.linkedin == True:
        
        from liclient import LinkedInAPI
        configs = Config_linkedin.objects.all()
        #return HttpResponse(configs[0].linkedin_app_secret)
        APIClient = LinkedInAPI(str(configs[0].linkedin_app_id), str(configs[0].linkedin_app_secret))
        request_token = APIClient.get_request_token()
        
        
        authorization_url = APIClient.base_url + APIClient.authorize_path
        url = "%s?oauth_token=%s" % (authorization_url, request_token['oauth_token'])
        
        request.session['request_token'] = request_token
        
        return HttpResponseRedirect('/sistema/campanhas/autoriza_linkedin/?url=' + url)
        
        
    self.message_user(request, "Campanha " + titulo + " " + mensagem )
            

class CampanhaAdmin(admin.ModelAdmin):    
    
    list_display = ('titulo','descricao','url','twitter','facebook', 'linkedin','criada_em','enviado_em', 'status')
    search_fields = ['titulo', 'descricao']
    
    fieldsets = (
        (None, {
            'fields': ('twitter','facebook', 'linkedin','titulo', 'descricao', 'url')
        }),
    )

    actions = [publicar]
    
admin.site.register(Campanha, CampanhaAdmin)
