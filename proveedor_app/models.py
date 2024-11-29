from django.db import models

# Create your models here.

class Proveedor(models.Model):
    codigo=models.PositiveSmallIntegerField(primary_key=True,max_length=60)
    nombre=models.CharField(max_length=100)
    productos=models.CharField(max_length=60)
    direccion=models.CharField(max_length=60)
    telefono=models.PositiveIntegerField()
    frecuencia=models.CharField(max_length=60)
    pagos=models.SmallIntegerField()

    def __str__(self):
        return self.nombre
