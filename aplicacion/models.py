from pyexpat import model
from django.db import models


class Familiar(models.Model):
    name = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    Tipofamilia = models.CharField( max_length=50)
    edad = models.IntegerField()
    id = models.IntegerField(primary_key=True)

# Create your models here.
