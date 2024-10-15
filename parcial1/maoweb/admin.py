from django.contrib import admin
from .models import vehiculo
from .models import sede
from .models import facturacion
from .models import proveedor
from .models import empleado
from .models import conductor
from .models import gastos
from .models import administrador
from .models import puntos
from .models import premios


admin.site.register(vehiculo)
admin.site.register(sede)
admin.site.register(facturacion)
admin.site.register(proveedor)
admin.site.register(empleado)
admin.site.register(conductor)
admin.site.register(gastos)
admin.site.register(administrador)
admin.site.register(puntos)
admin.site.register(premios)
# Register your models here.
