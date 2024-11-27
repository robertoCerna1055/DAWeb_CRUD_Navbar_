from django.db import models

# Create your models here.

class  Pedido(models.Model):
    id_pedido = models.CharField(primary_key=True,max_length=6)
    fecha_pedido = models.CharField(max_length=15)
    id_cliente = models.CharField(max_length=6)
    total_pedido = models.CharField(max_length=15)
    fecha_entrega = models.CharField(max_length=20)
    direccion_entrega = models.CharField(max_length=50)
    id_empleado = models.CharField(max_length=6)

    def __str__(self):
        return self.fecha_pedido
    