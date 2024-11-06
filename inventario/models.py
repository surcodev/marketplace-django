from django.db import models

class Rubro(models.Model):
    nombre=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    # estado = models.BooleanField(default=False)
    # imagen=models.ImageField(upload_to='imagenes/',verbose_name="imagenes categoria",null=True,blank=True)
    # tamano=models.ForeignKey(Tamano,on_delete=models.CASCADE,related_name='categoriatamaño',blank=True,default=1)
    # descripcion=models.TextField(verbose_name="Descripcion",null=True,blank=True)
    rubro=models.ForeignKey(Rubro,on_delete=models.CASCADE,related_name='categoria',blank=True,default=1)
    def __str__(self):
        return self.nombre

class Subcategoria(models.Model):
    nombre_subcategoria = models.CharField(max_length=100)
    # estado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias',blank=True)

    def __str__(self):
        return self.nombre_subcategoria
