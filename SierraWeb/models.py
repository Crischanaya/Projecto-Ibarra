from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    
    def nombreCompleto(self):
        txt = "{0} {1}/ Correo: {2}"
        return txt.format(self.nombre_usuario,self.apellido,self.correo)

    def __str__(self):
        return '%s. %s %s' %(self.id_usuario,self.nombre_usuario, self.apellido)

class Paquetes(models.Model):
    id_paquete = models.AutoField(primary_key=True)
    nombre = models.TextField()
    lugar = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    
    def nombrePaquetes(self):
        txt = "{0}/ Lugar: {1} / Precio: {2} "
        return txt.format(self.nombre,self.lugar,self.precio)

    def __str__(self):
        return '%s. %s , %s' %(self.id_paquete,self.nombre, self.lugar)

class UserPaquete(models.Model):
    id_userpaquete = models.AutoField(primary_key=True)
    id_paquete = models.ForeignKey(Paquetes ,on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios ,on_delete=models.CASCADE)

    def __str__(self):
        txt = " Usuario: {0} / Paquete: {1}"
        return txt.format(self.id_usuario.nombreCompleto(),self.id_paquete.nombrePaquetes())
        