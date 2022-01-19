from calendar import month
from datetime import datetime
from pydoc import describe
from pyexpat import model
from wsgiref.handlers import format_date_time
from django.db import models


# Create your models here.
class hola(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class jsoninfo(models.Model):
    end_year = models.CharField(max_length=200)
    intensity = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    insight = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    start_year = models.CharField(max_length=200)
    impact = models.CharField(max_length=200)
    added = models.CharField(max_length=200)
    published = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    relevance = models.CharField(max_length=200)
    pestle = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    likelihood = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.topic} , {self.sector}"

    
