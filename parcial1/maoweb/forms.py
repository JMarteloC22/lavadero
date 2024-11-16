from django import forms
from maoweb.models import vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = vehiculo
        fields = ['marca', 'v_ident', 'soat', 'tipo', 'vias_frecuentes', 'combustible', 'transmision']
        
        widgets = {
            'marca': forms.Select(choices=[
                ('Chevrolet', 'Chevrolet'),
                ('Audi', 'Audi'),
                ('Toyota', 'Toyota'),
                ('BMW', 'BMW'),
                ('Ford', 'Ford'),
                ('Honda', 'Honda'),
                ('Mercedes-Benz', 'Mercedes-Benz'),
                ('Nissan', 'Nissan'),
                ('Volkswagen', 'Volkswagen'),
                ('Hyundai', 'Hyundai'),
                ('Bajaj', 'Bajaj'),
                ('Honda', 'Honda'),
                ('Yamaha', 'Yamaha'),
                ('Suzuki', 'Suzuki'),
                ('Kawasaki', 'Kawasaki'),
                ('TVS', 'TVS'),
                ('Hero', 'Hero'),
                ('AKT', 'AKT'),
                ('KTM', 'KTM'),

                # Agrega más marcas según sea   necesario
            ]),
            'tipo': forms.Select(choices=[
                ('Carro', 'Carro'),
                ('Moto', 'Moto'),
                ('Pesado', 'Vehiculo Pesado'),
                # Agrega más tipos según sea necesario
            ]),
            'vias_frecuentes': forms.Select(choices=[
                ('Pista', 'Pista'),
                ('Carretera', 'Carretera'),
                ('Ciudad', 'Ciudad'),
                ('Destapada', 'Destapada'),
                # Agrega más vías según sea necesario
            ]),
            'combustible': forms.Select(choices=[
                ('gasolina', 'Gasolina'),
                ('diesel', 'Diésel'),
                ('Extra', 'Extra'),
                # Agrega más tipos de combustible según sea necesario
            ]),
            'transmision': forms.Select(choices=[
                ('manual', 'Manual'),
                ('automatico', 'Automático'),
                # Agrega más tipos de transmisión según sea necesario
            ]),
        }