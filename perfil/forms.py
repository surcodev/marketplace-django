from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from .models import User, Cliente, Administrador
from geografia.models import Departamento, Provincia, Distrito
#from django.contrib.auth.models import User

class ClienteRegistroForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, label="Teléfono")
    direccion = forms.CharField(max_length=255, label="Dirección")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': "Nombre de usuario",
            'email': "Correo electrónico",
            'password1': "Contraseña",
            'password2': "Confirmar contraseña",
        }
        widgets = {
            'username': forms.TextInput(attrs={'autofocus': False}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            # Creación directa de Cliente asociada al usuario
            Cliente.objects.create(
                user=user, 
                telefono=self.cleaned_data['telefono'], 
                direccion=self.cleaned_data['direccion']
            )
        return user

class AdminRegistroForm(UserCreationForm):
    # Campos adicionales
    nombre_negocio = forms.CharField(max_length=255)
    razon_social = forms.CharField(max_length=255)
    ruc = forms.CharField(max_length=11)
    direccion = forms.CharField(max_length=255)
    
    # Utilizar ModelChoiceField para generar listas desplegables
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), empty_label="Seleccione un departamento")
    provincia = forms.ModelChoiceField(queryset=Provincia.objects.none(), empty_label="Seleccione una provincia")  # Inicialmente vacío
    distrito = forms.ModelChoiceField(queryset=Distrito.objects.none(), empty_label="Seleccione un distrito")  # Inicialmente vacío

    telefono = forms.CharField(max_length=15)
    correo_personal = forms.EmailField(required=False)
    nombre_admin = forms.CharField(max_length=100, label="Nombre de administrador")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Asegúrate de no añadir autofocus al campo 'username'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)

        # Verificar si ya se ha pasado un valor de departamento para filtrar las provincias y distritos
        if 'departamento' in self.data:
            try:
                departamento_id = int(self.data.get('departamento'))
                self.fields['provincia'].queryset = Provincia.objects.filter(departamento_id=departamento_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # Si hay un error, simplemente usa un conjunto vacío
        else:
            self.fields['provincia'].queryset = Provincia.objects.none()

        if 'provincia' in self.data:
            try:
                provincia_id = int(self.data.get('provincia'))
                self.fields['distrito'].queryset = Distrito.objects.filter(provincia_id=provincia_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # Si hay un error, simplemente usa un conjunto vacío
        else:
            self.fields['distrito'].queryset = Distrito.objects.none()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admindisco = True
        user.is_active = False  # Desactivar la cuenta por defecto
        if commit:
            user.save()
            Administrador.objects.create(
                user=user,
                nombre_admin=self.cleaned_data['nombre_admin'],
                nombre_negocio=self.cleaned_data['nombre_negocio'],
                razon_social=self.cleaned_data['razon_social'],
                ruc=self.cleaned_data['ruc'],
                direccion=self.cleaned_data['direccion'],
                departamento=self.cleaned_data['departamento'],
                provincia=self.cleaned_data['provincia'],
                distrito=self.cleaned_data['distrito'],
                telefono=self.cleaned_data['telefono'],
                correo_personal=self.cleaned_data['correo_personal'],
            )
        return user