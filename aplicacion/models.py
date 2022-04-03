from pyexpat import model
from django.db import models


class Familiar(models.Model):
    name = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    tipofamilia = models.CharField( max_length=50)
    edad = models.IntegerField(null=True)
    fecha_nacimiento = models.DateField(null=True)
    id = models.AutoField(primary_key=True)

# Create your models here.
