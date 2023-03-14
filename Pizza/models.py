from django.db import models



class Bebida(models.Model):
        nombre_bebida= models.CharField(max_length=20)
        precio_bebida= models.IntegerField()
        marca_bebida= models.CharField(max_length=20)
        litros_bebida=  models.IntegerField()
        
        def __str__(self):
            return f"{self.id} - nombre:{self.nombre_bebida} - ${self.precio_bebida}"
        
        
        
class Pizza(models.Model):
        nombre_pizza= models.CharField(max_length=20)
        precio_pizza= models.IntegerField()
        descripcion_pizza= models.CharField(max_length=100)
        tamanio_pizza=  models.CharField(max_length=10)
        
        def __str__(self):
            return f"{self.id} - {self.nombre_pizza} - ${self.precio_pizza} - {self.tamaño_pizza}"
        
        
class Empanada(models.Model):
        nombre_empanada= models.CharField(max_length=20)
        precio_empanada= models.IntegerField()
        coccion_empanada= models.CharField(max_length=100)
        sabor_empanada=  models.CharField(max_length=10)
        
        def __str__(self):
            return f"{self.id} - nombre:{self.nombre_empanada} - {self.sabor_empanada} - ${self.precio_empanada} "