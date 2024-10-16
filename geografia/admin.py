from django.contrib import admin
from .models import Departamento, Provincia, Distrito

from unfold.admin import ModelAdmin
#from django.contrib.admin import ModelAdmin

class DepartamentoAdmin(ModelAdmin):
    list_display = ('get_departamento',)
    def get_departamento(self, obj):
        return obj.nombre
    get_departamento.short_description = 'Departamento'
    
class ProvinciaAdmin(ModelAdmin):
    list_display = ('get_departamento', 'get_provincia')
    def get_departamento(self, obj):
        return obj.departamento.nombre
    def get_provincia(self, obj):
        return obj.nombre
    get_departamento.short_description = 'Departamento'
    get_provincia.short_description = 'Provincia'
    
class DistritoAdmin(ModelAdmin):
    list_display = ('get_provincia', 'get_distrito')
    def get_provincia(self, obj):
        return obj.provincia.nombre
    def get_distrito(self, obj):
        return obj.nombre
    get_provincia.short_description = 'Provincia'
    get_distrito.short_description = 'Distrito'

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Distrito, DistritoAdmin)