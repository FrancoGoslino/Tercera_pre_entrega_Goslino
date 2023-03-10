from django.db import models

class Bebida(models.Model):
        nombre_bebida= models.CharField(max_length=20)
        precio_bebida= models.CharField(max_length=6)
        marca_bebida= models.CharField(max_length=20)
        litros_bebida=  models.CharField(max_length=6)
        
        def __str__(self):
            return f"{self.id} - {self.nombre_bebida} - ${self.precio_bebida}"