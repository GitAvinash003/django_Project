from django.db import models
import uuid
# Create your models here.

class Student(models.Model):
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    age = models.DecimalField(max_digits=20,decimal_places=0)
    gender =models.CharField(max_length=20)
    
    
    def __str__(self):
        return  self.name + '......'+self.email
        