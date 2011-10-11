from django.http import HttpResponse, HttpResponseRedirect
from redes_sociais.models import Twitter as Config_twitter, Facebook as Config_facebook, Linkedin as Config_linkedin
from redes_sociais.models import Twitter, Facebook, Linkedin
from django.contrib import admin

class TwitterAdmin(admin.ModelAdmin):
    list_display = ('usuario','consumer_key', 'consumer_secret', 'access_key','access_secret')
    
admin.site.register(Twitter, TwitterAdmin)

def set_token_facebook(self, request, queryset):
    
    configs = Config_facebook.objects.all()
    request.session['id_facebook'] = configs[0].id
    
    return HttpResponseRedirect('/sistema/redes_sociais/facebook/autoriza_facebook/')

class FacebookAdmin(admin.ModelAdmin):
    list_display = ('usuario','facebook_app_id', 'facebook_app_secret', 'access_token')
    
    actions = [set_token_facebook]
    
admin.site.register(Facebook, FacebookAdmin)


def set_token_linkedin(self, request, queryset):
    
    from liclient import LinkedInAPI
    configs = Config_linkedin.objects.all()
    APIClient = LinkedInAPI(str(configs[0].linkedin_app_id), str(configs[0].linkedin_app_secret))
    request_token = APIClient.get_request_token()
    
    authorization_url = APIClient.base_url + APIClient.authorize_path
    url = "%s?oauth_token=%s" % (authorization_url, request_token['oauth_token'])
    
    request.session['request_token'] = request_token
    request.session['id_linkedin'] = configs[0].id
    
    return HttpResponseRedirect('/sistema/redes_sociais/linkedin/autoriza_linkedin/?url=' + url)
    
class LinkedinAdmin(admin.ModelAdmin):
    list_display = ('usuario','linkedin_app_id', 'linkedin_app_secret', 'access_token', 'oauth_token_secret')
    
    actions = [set_token_linkedin]
    
admin.site.register(Linkedin, LinkedinAdmin)

