from django.db import models

# Create your models here.
class Habitacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='Apellido predeterminado') # definimos un valor predeterminado
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Reserva(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cliente} reservó {self.habitacion} del {self.fecha_inicio} al {self.fecha_finh3}'
