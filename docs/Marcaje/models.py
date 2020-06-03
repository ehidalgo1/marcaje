from django.db import models

# Create your models here.
class Marcaje(models.Model):
    fecha = models.DateField()
    entrada = models.TimeField()
    salida = models.TimeField(null=True, blank=True)
    usuario = models.CharField(max_length=255)