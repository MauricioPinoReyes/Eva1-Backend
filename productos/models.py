from django.db import models


class Producto(models.Model):
    nombre = models.TextField(max_length=100)
    marca = models.TextField(max_length=100)
    precio = models.IntegerField(null=False)

    