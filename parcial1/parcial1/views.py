# parcial1/views.py
from django.shortcuts import render

def menu_vista(request):
    opciones = ['vehiculo', 'facturacion', 'proveedor', 'empleado', 'sede', 'conductor', 'gastos', 'administrador', 'puntos', 'premios']
    return render(request, 'menu.html', {'opciones': opciones})
