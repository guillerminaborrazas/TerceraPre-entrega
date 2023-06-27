from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=40)
    RUT = models.IntegerField()
    email = models.EmailField(max_length=100)

class Articulo(models.Model):
    nombre = models.CharField(max_length=40)
    nro = models.IntegerField()
    precio = models.IntegerField()
    vendedor = models.CharField(max_length=100)

class Servicios(models.Model):
    descripcion = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=100)
    precio = models.IntegerField()

