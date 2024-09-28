from django.contrib import admin
from .models import vehiculo
from .models import sede
from .models import conductor
from .models import empleado

admin.site.register(vehiculo)
admin.site.register(sede)
admin.site.register(conductor)
admin.site.register(empleado)
# Register your models here.
