from django.db import models
from django.contrib.auth.models import AbstractUser

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    jefe = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
    
    def __str__(self):
        return self.nombre

class Empleado(AbstractUser):
    # Campos heredados de AbstractUser (username, password, email, first_name, last_name)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_contratacion = models.DateField(null=True)
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL)
    horario_laboral = models.JSONField(default=dict)  # Ej: {"lunes": ["08:00", "17:00"]}
    foto_perfil = models.ImageField(upload_to='empleados/fotos/', null=True, blank=True)
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.cedula})"
