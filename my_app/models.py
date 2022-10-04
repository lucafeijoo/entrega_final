from django.db import models


class mascotas(models.Model):

        nombre = models.CharField(max_length= 48)
        especie = models.CharField(max_length= 48)
        edad = models.IntegerField()

