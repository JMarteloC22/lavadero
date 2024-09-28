from django.db import models

# Create your models here.

class vehiculo (models.Model):
    marca = models.CharField(max_length=20)
    combustible = models.CharField(max_length=30)
    transmision = models.CharField(max_length=30)


class empleado (models.Model):
    nombre_empleado = models.CharField(max_length=70)
    edad_empleado = models.CharField(max_length=2)
    telefono = models.CharField(max_length=10)

class sede (models.Model):
    ubicacion = models.CharField(max_length=50)
    ganancias = models.CharField(max_length=20)
    impuestos = models.CharField(max_length=20)

class conductor (models.Model):
    nombre_conductor = models.CharField(max_length=70)
    edad_empleado = models.CharField(max_length=2)
    licencia = models.CharField(max_length=2)

    