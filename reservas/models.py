from django.db import models

# Create your models here.
# reservas/models.py

from django.db import models

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    cliente = models.CharField(max_length=100)
    fono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    personas = models.PositiveIntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='RESERVADO')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Reserva de {self.cliente} para {self.personas} personas'
