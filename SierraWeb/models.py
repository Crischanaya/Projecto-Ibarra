from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

class Paquetes(models.Model):
    id_paquete = models.AutoField(primary_key=True)
    nombre = models.TextField()
    lugar = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)

class UserPaquete(models.Model):
    id_userpaquete = models.AutoField(primary_key=True)
    id_paquete = models.ForeignKey('Paquetes', models.DO_NOTHING, db_column='id_paquete')
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
