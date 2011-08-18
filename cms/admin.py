
from cms.models import Conteudo
from django.contrib import admin

class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo','slogan', 'descricao_index')

admin.site.register(Conteudo,ConteudoAdmin)

