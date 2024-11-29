from django.db import models

# Create your models here.

class Venta(models.Model):
    factura=models.PositiveSmallIntegerField(primary_key=True,max_length=60)
    idcliente=models.PositiveSmallIntegerField(max_length=100)
    producto=models.CharField(max_length=60)
    empleado=models.CharField(max_length=60)
    fecha=models.DateField(max_length=60)
    cantidad=models.PositiveIntegerField()
    metodo=models.CharField(max_length=60)

    def __str__(self):
        return self.producto
