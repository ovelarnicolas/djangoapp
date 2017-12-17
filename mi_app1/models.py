from django.db import models
from django.utils.html import format_html

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    

class Telefono(models.Model):
    codigo_area = models.IntegerField(null = False)
    numero = models.IntegerField(null = False)
    usuario = models.ForeignKey(Usuario, related_name='telefonos')

class Auto(models.Model):
    modelo = models.CharField(max_length=100)
    patente = models.CharField(max_length=7)
    peso = models.IntegerField()

    def __str__(self):
        return self.modelo + ' ' + self.patente
