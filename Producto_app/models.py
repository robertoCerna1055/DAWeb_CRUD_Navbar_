from django.db import models

# Create your models here.

class  Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField(max_length=11)
    categoria = models.CharField(max_length=45)
    material = models.CharField(max_length=50)
    stock = models.IntegerField(max_length=15)
    id_proveedores = models.IntegerField(max_length=6)

    def __str__(self):
        return self.nombre
    