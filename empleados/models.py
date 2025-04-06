from django.contrib.auth.models import AbstractUser
from django.db import models

class Empleado(AbstractUser):
    # Campos adicionales para tu modelo
    departamento = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_contratacion = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.get_full_name() or self.username
