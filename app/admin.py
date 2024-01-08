from django.contrib import admin
from app.models import *
# Register your models here.

class customizedWebpage(admin.ModelAdmin):
    list_display = ['topic_name','name','url','email']
    list_display_links = ['name']
    list_editable = ['url']
    list_filter = ['topic_name']
    list_per_page = 1
    search_fields = ['name']

class customizedAcessrecord(admin.ModelAdmin):
    list_display = ['name','date','number','author']
    list_display_links = ['author']
    list_per_page = 1
    search_fields = ['author']

admin.site.register(Topic)

admin.site.register(Webpage,customizedWebpage)

admin.site.register(Acessrecord,customizedAcessrecord)


    

