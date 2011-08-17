
from redes_sociais.models import Twitter 
from django.contrib import admin

class TwitterAdmin(admin.ModelAdmin):
    list_display = ('usuario','consumer_key', 'consumer_secret', 'access_key','access_secret')
    
admin.site.register(Twitter, TwitterAdmin)
