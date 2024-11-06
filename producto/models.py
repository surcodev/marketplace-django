from django.db import models
from perfil.models import Negocio
from inventario.models import Categoria, Subcategoria

class Producto(models.Model):
    TAMAÑO_CHOICES = [
        ('GRANDE', 'Grande'),
        ('MEDIANO', 'Mediano'),
        ('MINI', 'Mini'),
    ]
    COLOR_CHOICES = [
        ('NEGRO', 'Negro'),
        ('DORADO', 'Dorado'),
        ('PLATEADO', 'Plateado'),
    ]
    ENVIO_CHOICES = [
        ('SI', 'Sí'),
        ('NO', 'No'),
    ]
    TIEMPO_ENTREGA_CHOICES = [
        ('8 H', '8 horas'),
        ('12 H', '12 horas'),
        ('24 H', '24 horas'),
        ('26 H', '26 horas'),
    ]

    nombre = models.CharField(max_length=100)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)
    subcategoria = models.OneToOneField(Subcategoria, on_delete=models.CASCADE)
    tamaño = models.CharField(max_length=10, choices=TAMAÑO_CHOICES)
    # color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    # medidas_grande = models.CharField(max_length=50, blank=True, null=True)
    # medidas_mediano = models.CharField(max_length=50, blank=True, null=True)
    # marca = models.CharField(max_length=50)
    # modelo = models.CharField(max_length=50)
    # descripcion = models.TextField()
    # stock = models.PositiveIntegerField()
    # fecha = models.DateField()
    # video = models.CharField(max_length=100, blank=True, null=True)
    # contenido = models.TextField(blank=True, null=True)
    # envio = models.CharField(max_length=2, choices=ENVIO_CHOICES)
    # tiempo_entrega = models.CharField(max_length=5, choices=TIEMPO_ENTREGA_CHOICES)
    # garantia = models.CharField(max_length=2, choices=ENVIO_CHOICES)
    # servicio = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"
