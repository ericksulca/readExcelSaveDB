from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=100, blank=True, null=True)
    id_web = models.IntegerField(blank=True, default=0)
    cantidad = models.FloatField(default=0,blank=True, null=True)
    min_cantidad = models.FloatField(default=0,blank=True, null=True)
    imagen = ResizedImageField(size=[100, None],upload_to='productos/', default="/imagen/default.jpg", blank=True, null=True)#upload_to='%Y/%m/%d',
    url = models.CharField(max_length=100, blank=True, null=True)
    exonerado = models.BooleanField(blank=True,default=False)
    valor = models.FloatField(default=1,blank=True)
    precio_compra_soles = models.FloatField(default=0,blank=True)
    precio_compra_dolares = models.FloatField(default=0,blank=True)
    precio_soles = models.FloatField(default=0,blank=True)
    precio_dolares = models.FloatField(default=0,blank=True)
    estado = models.BooleanField(blank=True,default=True)

    def __str__(self):
        return str(self.nombre)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200,blank=True, null=True)
    numerodocumento = models.CharField(max_length=11, blank=True, null=True)
    telefono = models.CharField(max_length=15,blank=True, null=True)
    imagen = ResizedImageField(size=[100, None],upload_to='clientes/', default="/imagen/default_cliente.jpg", blank=True, null=True)#upload_to='%Y/%m/%d',
    longitud = models.CharField(max_length=25, blank=True, null=True)
    latitud = models.CharField(max_length=25, blank=True, null=True)
    estado = models.BooleanField(blank=True,default=True)

    def __str__(self):
        return str(self.nombre)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    documento = models.CharField(max_length=45, blank=True, null=True)
    estado = models.BooleanField(blank=True,default=True)

    def __str__(self):
        return str(self.nombre)