from django.db import models

# Create your models here.

class vehiculo (models.Model):
    marca = models.CharField(max_length=20)
    v_ident = models.CharField(max_length=20)
    soat = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    vias_frecuentes = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    combustible = models.CharField(max_length=30)
    transmision = models.CharField(max_length=30)

class facturacion (models.Model):
    banco = models.CharField(max_length=20)
    medio_pago = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)
    numero_recibo = models.CharField(max_length=20)
    monto = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=130)
    id_usuario = models.CharField(max_length=30)
    sede = models.CharField(max_length=30)

class proveedor (models.Model):
    producto = models.CharField(max_length=20)
    sede_proveedor = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    representante = models.CharField(max_length=60)

class empleado (models.Model):
    nombre_empleado = models.CharField(max_length=70)
    ident_emp = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    cargo = models.CharField(max_length=60)
    especialidad = models.CharField(max_length=60)
    emp_email = models.CharField(max_length=60)
    contrato = models.CharField(max_length=60)
    Salario = models.CharField(max_length=60)
    experiencia = models.CharField(max_length=60)
    edad_empleado = models.CharField(max_length=60)
    telefono = models.CharField(max_length=10)

class sede (models.Model):
    ubicacion = models.CharField(max_length=50)
    ganancias = models.CharField(max_length=20)
    impuestos = models.CharField(max_length=20)
    id_sede = models.CharField(max_length=20)
    horario = models.CharField(max_length=20)
    administrador_sede = models.CharField(max_length=20)
    sede_proveedor = models.CharField(max_length=20)
    gastos_sede = models.CharField(max_length=20)

class conductor (models.Model):
    nombre_conductor = models.CharField(max_length=70)
    edad_empleado = models.CharField(max_length=2)
    licencia = models.CharField(max_length=2)
    ident_cond = models.CharField(max_length=10)
    telefono_cond = models.CharField(max_length=20)
    email_cond = models.CharField(max_length=20)
    fidelidad = models.CharField(max_length=20)

class gastos (models.Model):
    desc_gasto = models.CharField(max_length=120)
    valor = models.CharField(max_length=20)
    iva = models.CharField(max_length=20)
    gastos_sede = models.CharField(max_length=20)

class administrador (models.Model):
    ubicacion = models.CharField(max_length=20)
    ident_emp = models.CharField(max_length=20)

class puntos (models.Model):
    nombre_conductor = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=20)
    v_ident = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=20)

class premios (models.Model):
    cantidad = models.CharField(max_length=20)
    premio = models.CharField(max_length=20)
    Desc_premio = models.CharField(max_length=20)