from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50) 
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.usuario} {self.contraseña}" 
    

class Cancha(models.Model):
    numero = models.IntegerField() # 1, 2, 3, 4, 5, 6.
    tipo = models.CharField(max_length=50) #pasto sintetico, pasto natural, cemento
    precio = models.IntegerField() # 30.000 , algun descuento por primer vez, a 15.000

    def __str__(self):
        return f"{self.numero} {self.tipo} {self.precio}"

class Disponibilidad(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE) # para que se elimine lo que viene de la cancha
    dia_semana = models.DateField()       # 1=Lunes, 2=Martes, ..., 7=Domingo
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    reservado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cancha} {self.dia_semana} {self.hora_inicio} {self.hora_fin} {self.reservado}"

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    disponibilidad = models.ForeignKey(Disponibilidad, on_delete=models.CASCADE)
    pagado = models.BooleanField()
    pago = models.OneToOneField(Pago, on_delete=models.CASCADE, null=True, blank=True) 

    def save(self, *args, **kwargs):
        self.disponibilidad.reservado = True  # Actualizar el atributo reservado
        self.disponibilidad.save()  # Fix: Access the related object and call save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente}, {self.disponibilidad},{self.pagado},{self.pago}"
class Pago (models.Model):
    reserva = models.ForeignKey ('Reserva', on_delete=models.CASCADE)
    monto = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.reserva} {self.monto} {self.fecha} {self.hora}"
    