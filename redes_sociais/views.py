from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from redes_sociais.models import Twitter as Config_twitter, Linkedin as Config_linkedin, Facebook as Config_facebook


def autoriza_linkedin(request):
    
    return render_to_response('redes_sociais/linkedin.html', {
                                                          "url": request.REQUEST.get('url'),
                                                          "session": request.REQUEST.get('session')
                                                          }
                              )

def confirma_linkedin(request):
   
    from liclient import LinkedInAPI
    configs = Config_linkedin.objects.get(pk=request.session['id_linkedin'])

    APIClient = LinkedInAPI(str(configs.linkedin_app_id), str(configs.linkedin_app_secret))
    
    access_token = APIClient.get_access_token(request.session['request_token'], request.REQUEST.get('codigo_confirmacao'))
    
    configs.access_token = access_token.oauth_token
    configs.oauth_token_secret = access_token.oauth_token_secret
    
    configs.save()

    return HttpResponseRedirect('/sistema/painel/redes_sociais/linkedin/')         



def autoriza_facebook(request):
    
    configs = Config_facebook.objects.get(pk=request.session['id_facebook'])
    
    return render_to_response('redes_sociais/facebook.html', {
                                                          "appid": configs.facebook_app_id
                                                          
                                                          }
                              )
    
def confirma_facebook(request):
   
    configs = Config_facebook.objects.get(pk=request.session['id_facebook'])
    
    configs.access_token = request.REQUEST.get('codigo_confirmacao')
    configs.save()
    return HttpResponseRedirect('/sistema/painel/redes_sociais/facebook/')
                              
def popup_facebook(request):
    
    return render_to_response('redes_sociais/popup_facebook.html', {
                                                          "appid": request.REQUEST.get("appid")
                                                          
                                                          }
                              )