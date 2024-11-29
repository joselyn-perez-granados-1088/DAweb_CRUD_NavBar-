from django.db import models

# Create your models here.


class Empleado(models.Model):
    codigo=models.PositiveSmallIntegerField(primary_key=True,max_length=60)
    nombre=models.CharField(max_length=100)
    cargo=models.CharField(max_length=60)
    horario=models.CharField(max_length=60)
    salario=models.PositiveSmallIntegerField()
    experiencia=models.CharField(max_length=60)
    certificaciones=models.CharField(max_length=60)

    def __str__(self):
        return self.nombre
