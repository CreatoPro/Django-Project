from pydoc import describe
from pyexpat import model
from django.db import models

# Create your models here.
class hola(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    