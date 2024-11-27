from django.db import models

# Create your models here.

class  Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    cargo = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    c_electronico = models.CharField(max_length=50)
    fecha_contratacion = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    