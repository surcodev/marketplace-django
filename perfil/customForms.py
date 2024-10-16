from django import forms
from .models import Cliente, Administrador, User
from django.contrib import messages
from django.core.exceptions import ValidationError

class AdministradorForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    email = forms.EmailField(label="Correo electrónico")
    is_active = forms.BooleanField(label="Cuenta Activa", required=False)  # Campo agregado para is_active

    class Meta:
        model = Administrador
        fields = ['username', 'email', 'nombre_admin', 'nombre_negocio', 'razon_social', 'ruc', 'direccion', 'departamento', 'provincia', 'distrito', 'telefono', 'correo_personal', 'is_active']

    def __init__(self, *args, **kwargs):
        super(AdministradorForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Inicializamos los campos con los datos del usuario
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
            self.fields['is_active'].initial = self.instance.user.is_active  # Inicializamos is_active

    def save(self, commit=True):
        # Guardar el administrador sin hacer commit
        administrador = super(AdministradorForm, self).save(commit=False)

        # Guardar el username, email y is_active del usuario relacionado
        user = administrador.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.is_active = self.cleaned_data['is_active']  # Guardar el valor de is_active
        user.save()  # Es necesario guardar el usuario explícitamente
        
        # Guardar los demás datos del administrador
        if commit:
            administrador.save()

        return administrador


class ClienteForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de Cliente", max_length=150)
    email = forms.EmailField(label="Correo electrónico")
    is_active = forms.BooleanField(label="Cuenta Activa", required=False)

    

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
            self.fields['is_active'].initial = self.instance.user.is_active

    # Validación del correo electrónico en uso
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.instance and self.instance.user:
            user = self.instance.user
            if User.objects.filter(email=email).exclude(pk=user.pk).exists():
                raise forms.ValidationError('El correo electrónico ya está en uso por otro usuario.')
        return email

    def save(self, commit=True):
        cliente = super(ClienteForm, self).save(commit=False)
        user = cliente.user

        # Actualizar los datos del usuario
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.is_active = self.cleaned_data['is_active']
        user.save()

        if commit:
            cliente.save()

        return cliente