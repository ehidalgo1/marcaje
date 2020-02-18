from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    usuario=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

class Marcaje(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    tipo=models.CharField(max_length=255)
    usuario=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)