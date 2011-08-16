from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from campanhas.models import Campanhas
from api.api import Twitter

def index(request):

    if request.user.is_authenticated():
        campanhas = Campanhas.objects.all()
        total = Campanhas.objects.count()
    
        return render_to_response('campanhas/index.html', {"campanhas" :campanhas, "total":total})
    else:
        return HttpResponseRedirect("/erro_autenticacao/")

def nova(request):
    
    if request.user.is_authenticated():

        return render_to_response('campanhas/nova.html')
    else:
        return HttpResponseRedirect("/erro_autenticacao/")

def cadastrarNova(request):
    
    if request.user.is_authenticated():
    
        if request.method == 'POST':
                string = request.POST
                
                tit = string.get("titulo")
                desc = string.get("descricao")
                redes = string.getlist("redes_sociais")
                arrayRedes = []
                
                for rede in redes:
                    arrayRedes.append(rede)
                    if rede == 'Twitter':
                        a = Twitter()
                        a.enviaTweet(desc)
                    
                p = Campanhas(redes_sociais= arrayRedes, titulo=tit, descricao=desc)
                p.save()
        
        return HttpResponseRedirect("/campanhas/")
    
    else:
        
        return HttpResponseRedirect("/erro_autenticacao/")
