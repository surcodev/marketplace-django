from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django import forms

from .forms import ClienteRegistroForm, AdminRegistroForm
from .models import User, Cliente, Administrador
from django.http import JsonResponse
from geografia.models import Provincia, Distrito

def cargar_provincias(request):
    departamento_id = request.GET.get('departamento_id')
    provincias = Provincia.objects.filter(departamento_id=departamento_id).order_by('nombre')
    return JsonResponse(list(provincias.values('id', 'nombre')), safe=False)

def cargar_distritos(request):
    provincia_id = request.GET.get('provincia_id')
    distritos = Distrito.objects.filter(provincia_id=provincia_id).order_by('nombre')
    return JsonResponse(list(distritos.values('id', 'nombre')), safe=False)


@login_required
def cliente_panel(request):
    return render(request, 'cliente_panel.html')

@login_required
def admin_panel(request):
    return render(request, 'admin_panel.html')

###########################################################

# INDEX PRINCIPAL
def index(request):
    return render(request, 'index.html')

# PLANTILLA REGISTRO (CLIENTE - ADMINISTRADOR DISCOTECA)
def registro(request):
    return render(request, 'registro.html')

# REGISTRO DE CLIENTE
def cliente_registro(request):
    form = ClienteRegistroForm(request.POST or None)
    
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Cuenta pendiente de activación por el administrador')
        return redirect('login')
    
    return render(request, 'cliente_registro.html', {'form': form})

# REGISTRO DE ADMIISTRADOR DISCOTECA
def administrador_registro(request):
    form = AdminRegistroForm(request.POST or None)
    
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('login')
    
    return render(request, 'admin_registro.html', {'form': form})

# LOGIN PANEL
class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            # Intenta obtener el usuario directamente aquí
            try:
                self.user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("El correo electrónico no está registrado.")

        return self.cleaned_data

def login_view(request):
    form = EmailAuthenticationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        # Usar el usuario obtenido en el formulario
        user = form.user
        
        # Autenticación
        user = authenticate(username=user.username, password=password)

        if user:
            login(request, user)
            if user.is_admindisco:
                return redirect('admin_panel')
            elif not user.is_superuser:
                return redirect('cliente_panel')
        else:
            messages.error(request, 'Credenciales incorrectas')

    return render(request, 'login.html', {'form': form})
