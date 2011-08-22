
from cms.models import Configuracoes
from django.contrib import admin

class ConfiguracoesAdmin(admin.ModelAdmin):
    list_display = ('titulo','slogan', 'descricao_index')

admin.site.register(Configuracoes,ConfiguracoesAdmin)

