# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
        
    template = {"titulo" : 'OpenSocialCRM',
               "slogan" : 'Gestão social open-source',
               "descricao_index" : 'OpenSocialCRM é uma ferramenta livre para gerenciamento de campanhas de marketing em redes sociais', 
               "usuario_logado" : request.user.username
              }
            
    return render_to_response('index/index.html', {'template': template})
