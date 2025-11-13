from django.db import models

class Empleado(models.Model):
    id_emp = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    id_atr = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Atraccion(models.Model):
    id_atr = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=20)
    altura_min = models.DecimalField(max_digits=4, decimal_places=2)
    id_emp = models.IntegerField(null=True, blank=True)  # 🔹 temporal, quitar FK por ahora

    def __str__(self):
        return self.nombre

    
class Cliente(models.Model):
        id_cli = models.AutoField(primary_key=True, unique=True) 
        nombre = models.CharField(max_length=50) 
        apellido = models.CharField(max_length=50)    
        telefono = models.CharField(max_length=15) 
        correo = models.CharField(max_length=50) 
        fecha_reg = models.DateField(auto_now_add=True) 
        id_atr = models.IntegerField(null=True, blank=True)


        def __str__(self):
            return self.nombre