from django.db import models

# Create your models here.
class Persona(models.Model):
   
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    

class Trabajo(models.Model):
    
    trabajo = models.CharField(max_length=30)



class Hobby(models.Model):
    
    hobby = models.CharField(max_length=30)    