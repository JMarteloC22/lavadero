from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from .forms import VehiculoForm
from .models import vehiculo

def menu_vista(request):
    opciones = ['vehiculo', 'facturacion', 'proveedor', 'empleado', 'sede', 'conductor', 'gastos', 'administrador', 'puntos', 'premios']
    return render(request, 'menu.html', {'opciones': opciones})

def registrar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el vehículo en la base de datos
            messages.success(request, 'Dato insertado, ')  # Mensaje de éxito
            return redirect('menu')  # Redirige a una vista de éxito
    else:
        form = VehiculoForm()  # Crea un formulario vacío

    return render(request, 'Vehiculo_insertar.html', {'form': form})

def listar_vehiculos(request):
    vehiculos = vehiculo.objects.all()  # Obtiene todos los vehículos
    return render(request, 'listar_vehiculos.html', {'vehiculos': vehiculos})

def eliminar_vehiculo(request, vehiculo_id):
    vehiculo_a_eliminar = get_object_or_404(vehiculo, id=vehiculo_id)
    vehiculo_a_eliminar.delete()  # Elimina el vehículo
    messages.success(request, 'Vehículo eliminado con éxito.')
    return redirect('listar_vehiculos')  # Redirige a la lista de vehículos

def eliminar_por_identificacion(request):
    if request.method == 'POST':
        v_ident = request.POST.get('v_ident', '').strip()  # Obtiene la identificación del formulario
        try:
            # Busca el vehículo ignorando mayúsculas y minúsculas
            vehiculo_a_eliminar = vehiculo.objects.get(v_ident__iexact=v_ident)
            vehiculo_a_eliminar.delete()  # Elimina el vehículo
            messages.success(request, 'Vehículo eliminado con éxito.')
        except vehiculo.DoesNotExist:
            messages.error(request, 'No se encontró un vehículo con esa identificación.')
        return redirect('eliminar_por_identificacion')  # Redirige a la misma página

    return render(request, 'eliminar_por_identificacion.html')

def actualizar_vehiculo(request):
    if request.method == 'POST':
        v_ident = request.POST.get('v_ident', '').strip()  # Obtiene la identificación del formulario
        try:
            vehiculo_a_actualizar = vehiculo.objects.get(v_ident__iexact=v_ident)
            if request.method == 'POST':
                form = VehiculoForm(request.POST, instance=vehiculo_a_actualizar)
                if form.is_valid():
                    form.save()  # Guarda los cambios
                    messages.success(request, 'Dato modificado con éxito.')
                    return redirect('menu')  # Redirige al menu
        except vehiculo.DoesNotExist:
            messages.error(request, 'No se encontró un vehículo con esa identificación.')
            return redirect('actualizar_vehiculo')  # Redirige a la misma página

    else:
        form = VehiculoForm()  # Crea un formulario vacío

    return render(request, 'actualizar_vehiculo.html', {'form': form})