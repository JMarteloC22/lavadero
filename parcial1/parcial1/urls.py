from django.urls import path
from django.contrib import admin
#from django.urls import path.include
#from . import views
from maoweb.views import registrar_vehiculo, listar_vehiculos, eliminar_vehiculo, eliminar_por_identificacion, actualizar_vehiculo
from maoweb.views import menu_vista

urlpatterns = [
# path('menu/', views.menu_vista, name='menu'),
    path('admin/', admin.site.urls),
    path('', menu_vista, name='menu'),
    path('insertar/vehiculo', registrar_vehiculo, name='insertar_vehiculo'),
    path('listar/vehiculo', listar_vehiculos, name='listar_vehiculos'),
    path('eliminar/vehiculo/<int:vehiculo_id>/', eliminar_vehiculo,name='eliminar_vehiculo'), 
    path('eliminar/vehiculo/', eliminar_por_identificacion, name='eliminar_por_identificacion'),
    path('actualizar/vehiculo', actualizar_vehiculo, name='actualizar_vehiculo'),
]
