from django.contrib import admin
from .models import Local, Evento, CategoriaEventos


# Register your models here.


class LocalesAdmin(admin.ModelAdmin):
    fieldssets =[]
    inlines = []
    list_display = ('nombre_local', 'activo', 'nombre_propietario')
    list_filter = ['nombre_local','activo']
    search_fields = ['nombre_local']


class EventosAdmin(admin.ModelAdmin):
    fieldssets = []
    inlines = []
    list_display = ('nombre_evento', 'activo')
    list_filter = ['hora_inicio','activo']
    search_fields = ['nombre_evento']


admin.site.register(Local,LocalesAdmin)
admin.site.register(Evento,EventosAdmin)
admin.site.register(CategoriaEventos)
