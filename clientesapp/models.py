from django.db import models


class Cliente(models.Model):
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=100, default='direccion')


class Orden(models.Model):
    num_orden = models.CharField(max_length=20, default='')
    fechain = models.CharField(max_length=30, default='')
    fechaout = models.CharField(max_length=30, default='')
    instrumento = models.CharField(max_length=30, default='')
    marca = models.CharField(max_length=20)
    referencia = models.CharField(max_length=30, default='')
    serial = models.CharField(max_length=15, default='')
    encargado = models.CharField(max_length=50, default='')
    abono = models.CharField(max_length=15, default='')
    procesos = models.TextField(default='')
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE, default='')


