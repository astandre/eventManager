from django.contrib import admin
from .models import Local, Evento, Direccion, Calificacion


# Register your models here.
class LocalesAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = []
    list_display = ('nombre', 'activo', 'nombre_propietario')
    list_filter = ['nombre', 'activo']
    search_fields = ['nombre']


class EventosAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = []
    list_display = ('nombre', 'activo', 'familiar', 'local', 'categoria')
    list_filter = ['fecha_inicio', 'activo', 'familiar', 'local__nombre', 'categoria']
    search_fields = ['nombre']


class CalificacionAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = []
    list_display = ('calificacion', 'evento', 'local')
    list_filter = ['evento', 'local']
    search_fields = ['evento', 'local']


# class DireccionAdmin(admin.ModelAdmin):
#     fieldsets = []
#     inlines = []
#     list_display = ('calificacion', 'evento', 'local')
#     list_filter = ['evento', 'local']
#     search_fields = ['evento', 'local']


admin.site.register(Local, LocalesAdmin)
admin.site.register(Evento, EventosAdmin)
admin.site.register(Direccion)
admin.site.register(Calificacion, CalificacionAdmin)
