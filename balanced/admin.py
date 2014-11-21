from django.contrib import admin
from models import *


class ObjetivoAdmin(admin.ModelAdmin):
    list_display = ['dimension', 'ciclo', 'objetivo']
    ordering = ['dimension', 'ciclo']

class ProyectoAdmin(admin.ModelAdmin):
    list_filter = ['lider']

@admin.register(Avance)
class AvanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'ciclo', 'proyecto', 'avance']

@admin.register(Ciclo)
class CicloAdmin(admin.ModelAdmin):
    list_display = ['clave', 'fecha_revision', 'observacion', 'status']

admin.site.register(Dimension)
admin.site.register(Objetivo, ObjetivoAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Perfil)
admin.site.register(Observacion)




