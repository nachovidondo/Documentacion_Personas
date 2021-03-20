from django.db import models
from apps.base.models import Basemodel
# Create your models here.



class Profesiones(Basemodel):
    titulo = models.CharField(max_length=100)
    
    class Meta:
        verbose_name ="Titulo"
        
    def __str__(self):
        return self.titulo
    
class Persona(Basemodel):
    nombre = models.CharField(max_length=100)
    edad= models.IntegerField()
    monotributista = models.BooleanField(default=True)
    profesion_personas = models.ForeignKey(Profesiones,on_delete=models.CASCADE,verbose_name= "Profesion")
    
    class Meta:
        verbose_name ="Personas"
        
    def __str__(self):
        return self.nombre
    
    
    