from django.shortcuts import render_to_response
from django.http import HttpResponse
from cms.models import Conteudo

def index(request):
    configs = Configuracoes.objects.all()
    template ={}
    for config in configs:
        
            template = {"titulo" : config.titulo,
                      "slogan" : config.slogan,
                      "descricao_index" : config.descricao_index, 
                      "usuario_logado" : request.user.username
                      }
            
    return render_to_response('index/index.html', {'template': template})

def erroAutenticacao(request):

    configs = Configuracoes.objects.all()
    template ={}
    for config in configs:
            template = {"titulo" : config.titulo,
                      "slogan" : config.slogan,
                      "descricao_index" : config.descricao_index }
            
    return render_to_response('erros/autenticacao.html', {'template': template})