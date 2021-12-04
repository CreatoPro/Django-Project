from django.db import models
from django.contrib.auth.models import AbstractUser




class User_Data(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    number= models.IntegerField()
        
    def __str__(self):
        return f"{self.name}{self.age}"


class Session(models.Model):
    in_time= models.TimeField()
    out_time= models.TimeField()

    def __str__(self):
        return self.user.email

class Recipt(models.Model):
    time= models.ForeignKey(Session, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.time

    

