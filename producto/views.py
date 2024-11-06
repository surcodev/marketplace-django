from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages

def home(request):
    productosListados = Producto.objects.all()
    messages.success(request, '¡Productos listados!')
    return render(request, "productos/gestionProductos.html", {"productos": productosListados})