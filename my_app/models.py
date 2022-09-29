from django.db import models

# Create your models here.
class nosotros(models.Model):

        nombre=models.CharField(max_length=40)
        trabajo=models.CharField(max_length=40)
        edad=models.IntegerField() 


class blogs(models.Model):

        topico=models.CharField(max_length=60)
        cantidad=models.IntegerField()
