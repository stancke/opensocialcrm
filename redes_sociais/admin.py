
from redes_sociais.models import Twitter, Facebook, Linkedin
from django.contrib import admin

class TwitterAdmin(admin.ModelAdmin):
    list_display = ('usuario','consumer_key', 'consumer_secret', 'access_key','access_secret')
    
admin.site.register(Twitter, TwitterAdmin)

class FacebookAdmin(admin.ModelAdmin):
    list_display = ('usuario','facebook_app_id', 'facebook_app_secret')
    
admin.site.register(Facebook, FacebookAdmin)


class LinkedinAdmin(admin.ModelAdmin):
    list_display = ('usuario','linkedin_app_id', 'linkedin_app_secret')
    
admin.site.register(Linkedin, LinkedinAdmin)

