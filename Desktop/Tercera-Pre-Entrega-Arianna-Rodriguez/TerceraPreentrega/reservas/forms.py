from django import forms
from .models import Habitacion, Reserva, Cliente

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ('nombre', 'descripcion', 'precio')

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('cliente', 'habitacion', 'fecha_inicio', 'fecha_fin')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'email', 'telefono')
