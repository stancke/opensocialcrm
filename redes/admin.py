
from redes.models import RedesSociais
from django.contrib import admin

class RedesSociaisAdmin(admin.ModelAdmin):
    list_display = ('rede_social','usuario', 'email')


admin.site.register(RedesSociais, RedesSociaisAdmin)
