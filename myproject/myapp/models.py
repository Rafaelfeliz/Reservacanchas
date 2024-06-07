from django.db import models

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
    numero = models.IntegerField()

    def __str__(self):
        return f"{self.numero}"

class Disponibilidad(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE) # para que se elimine lo que viene de la cancha
    dia_semana = models.DateField()       # 1=Lunes, 2=Martes, ..., 7=Domingo
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    disponible = models.BooleanField()

    def __str__(self):
        return f"{self.cancha} {self.dia_semana} {self.hora_inicio} {self.hora_fin} {self.disponible}"

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Disponibilidad = models.ForeignKey(Disponibilidad, on_delete=models.CASCADE)
    pagado = models.BooleanField()

    def __str__(self):
        return f"{self.cliente} {self.Disponibilidad} {self.pagado}"
    