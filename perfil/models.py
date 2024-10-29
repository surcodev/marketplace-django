from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import RegexValidator

import uuid
from geografia.models import Departamento, Provincia, Distrito

################################################################################

# perfil.User
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    is_admin_negocio = models.BooleanField('Admin. de negocio', null=True, blank=True, default=None)
    is_active = models.BooleanField('Usuario Activo', default=True)
    first_name = None
    last_name = None
    last_login = None

    class Meta:
        verbose_name_plural = "Usuarios"

# perfil.Cliente
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    nombre_cliente = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Clientes del Marketplace"
    
    # Sobrescribimos el método delete para eliminar también el usuario asociado
    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete(*args, **kwargs)


class Rubro(models.Model):
    nombre=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

# perfil.Negocio
class Negocio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el modelo User
    nombre_admin = models.CharField(max_length=255)
    nombre_negocio = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255)
    ruc = models.CharField(max_length=11, unique=True)

    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)  # Relación con el modelo Rubro

    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, null=True, blank=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    dni = models.CharField(max_length=15)
    foto_dni = models.ImageField(upload_to='uploads/dni')

    def clean(self):
        # Validar que la provincia pertenece al departamento seleccionado
        if self.provincia and self.departamento and self.provincia.departamento != self.departamento:
            raise ValidationError({
                'provincia': 'La provincia seleccionada no pertenece al departamento seleccionado.'
            })
        
        # Validar que el distrito pertenece a la provincia seleccionada
        if self.distrito and self.provincia and self.distrito.provincia != self.provincia:
            raise ValidationError({
                'distrito': 'El distrito seleccionado no pertenece a la provincia seleccionada.'
            })

    class Meta:
        verbose_name_plural = "Administradores de Negocio"

# Señal para eliminar el usuario relacionado cuando se elimina un negocio
@receiver(post_delete, sender=Negocio)
def borrar_usuario_relacionado(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()

@receiver(post_delete, sender=Cliente)
def borrar_usuario_relacionado(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()
