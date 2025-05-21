from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Donetask(models.Model):
    
    def __str__(self,):
        return str(user)+'s'+'tasks'
    
    
user=models.OneToOneField(to=User,on_delete=models.CASCADE)
donetask=models.CharField(max_length=255,blank=True,null=True)
    