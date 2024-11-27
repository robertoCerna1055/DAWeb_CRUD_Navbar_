from django.db import models

# Create your models here.

class  Venta(models.Model):
    id_venta = models.CharField(primary_key=True,max_length=6)
    fecha_venta = models.CharField(max_length=45)
    id_cliente = models.IntegerField(max_length=6)
    id_producto = models.IntegerField(max_length=6)
    cantidad = models.IntegerField(max_length=6)
    precio_unitario = models.IntegerField(max_length=6)
    forma_pago = models.CharField(max_length=45)

    def __str__(self):
        return self.fecha_venta
    