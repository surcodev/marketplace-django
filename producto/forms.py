from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

    CATEGORIAS = [
        ("electronics", "Electrónica"),
        ("clothing", "Ropa"),
        ("home", "Hogar"),
        ("toys", "Juguetes"),
        ("books", "Libros"),
    ]

    # Definimos las subcategorías para cada categoría

    categoria = forms.ChoiceField(
        choices=CATEGORIAS, widget=forms.Select(attrs={"class": "form-control"})
    )
    subcategoria = forms.ChoiceField(
        choices=[], widget=forms.Select(attrs={"class": "form-control"})
    )  # Lo dejamos vacío

    # Los demás campos se renderizarán por defecto
    tamaño = forms.ChoiceField(
        choices=[("S", "Pequeño"), ("M", "Mediano"), ("L", "Grande")],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    color = forms.ChoiceField(
        choices=[("rojo", "Rojo"), ("azul", "Azul"), ("verde", "Verde"), ("amarillo", "Amarillo")],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3})
    )
    stock = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )
    video = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        required=False,
    )

    imagen1 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        required=False,
    )
    imagen2 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        required=False,
    )
    imagen3 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        required=False,
    )
    imagen4 = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        required=False,
    )

    envio = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}), required=False
    )
    garantia = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}), required=False
    )
    servicio_tecnico = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}), required=False
    )

    tiempo_entrega = forms.ChoiceField(
        choices=[(8, "8 horas"), (12, "12 horas"), (24, "24 horas"), (48, "48 horas")],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
