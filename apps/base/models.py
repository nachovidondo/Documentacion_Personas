from django.db import models

# Create your models here.
class Basemodel(models.Model):
    
    id = models.AutoField(primary_key=True)
    status =models.BooleanField(default=True)
    create_date = models.DateField(verbose_name="fecha de creacion" , auto_now=True)
    update_date= models.DateField(verbose_name="fecha modificacion " ,auto_now_add=True)
    
    class Meta:
        verbose_name = "Modelo base"
        
    def __str__(self):
        return self.id