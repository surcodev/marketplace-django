from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.admin import SimpleListFilter
from .models import User, Cliente, Administrador
from .customForms import ClienteForm, AdministradorForm
from django.utils.html import format_html

from unfold.admin import ModelAdmin
#from django.contrib.admin import ModelAdmin

##########################################################################
# FILTRO PERSONALIZADO 
# 'is_active'
class CuentaActivaFilter(SimpleListFilter):
    title = 'Cuenta Activa'  # Nombre que se mostrará en la interfaz de administración
    parameter_name = 'user_is_active'  # Parámetro que se usa en la URL para el filtro

    def lookups(self, request, model_admin):
        return (
            ('1', 'Activo'),
            ('0', 'Inactivo'),
        )
    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(user__is_active=True)
        if self.value() == '0':
            return queryset.filter(user__is_active=False)

# 'is_admindisco'
class CuentaUserFilter(SimpleListFilter):
    title = 'Tipo de usuario'
    parameter_name = 'is_admindisco'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Administrador de Discoteca'),
            ('0', 'Cliente'),
        )
    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(is_admindisco=True)
        if self.value() == '0':
            return queryset.filter(is_admindisco=False)

##########################################################################
# MODELOS PERSONALIZADOS
# DISCOTECA
class AdministradorAdmin(ModelAdmin):
    form = AdministradorForm  # Utilizar el nuevo formulario personalizado
    list_display = ('get_username', 'get_nombre_negocio', 'get_ruc', 'get_razon_social', 'get_email', 'get_is_active')
    list_filter = (CuentaActivaFilter,)

    def get_username(self, obj):
        return obj.nombre_admin

    def get_nombre_negocio(self, obj):
        return obj.nombre_negocio

    def get_ruc(self, obj):
        return obj.ruc

    def get_razon_social(self, obj):
        return obj.razon_social

    def get_email(self, obj):
        return obj.user.email

    def get_is_active(self, obj):
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            'green' if obj.user.is_active else 'red',
            'Activo' if obj.user.is_active else 'Inactivo'
        )

    get_username.short_description = 'Administrador de Discoteca'
    get_nombre_negocio.short_description = 'Negocio'
    get_ruc.short_description = 'RUC'
    get_razon_social.short_description = 'Razón Social'
    get_email.short_description = 'Correo Electrónico'
    get_is_active.short_description = 'Estado de Cuenta'


# CLIENTE
class ClienteAdmin(ModelAdmin):
    form = ClienteForm  # Utilizar el nuevo formulario personalizado
    list_display = ('get_username', 'get_email', 'get_telefono', 'get_is_active')

    def get_username(self, obj):
        return obj.user.username   
    def get_email(self, obj):
        return obj.user.email  
    def get_telefono(self, obj):
        return obj.telefono
    def get_is_active(self, obj):
        return obj.user.is_active 

    get_username.short_description = 'Cliente'
    get_email.short_description = 'Email'
    get_telefono.short_description = 'Teléfono'
    get_is_active.boolean = True
    get_is_active.short_description = 'Estado de Cuenta'

# MODELO USUARIO
class UserAdmin(ModelAdmin):
    list_display = ('username', 'email', 'get_is_active')
    search_fields = ['username']
    list_filter = (CuentaUserFilter,)

    def get_is_active(self, obj):
        return obj.is_active

    get_is_active.boolean = True
    get_is_active.short_description = 'Cuenta Activa'

#########################################################################

admin.site.register(User, UserAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Administrador, AdministradorAdmin)
