from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    
    def nombreCompleto(self):
        txt = "{0} {1} / Correo: {2}"
        return txt.format(self.nombre_usuario,self.apellido,self.correo)

    def __str__(self):
        return '%s. %s %s' %(self.id_usuario,self.nombre_usuario, self.apellido)

class Paquetes(models.Model):
    id_paquete = models.AutoField(primary_key=True)
    nombre = models.TextField()
    lugar = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    def nombrePaquetes(self):
        txt = "{0}  /  Lugar: {1}  /  Precio: {2} "
        return txt.format(self.nombre,self.lugar,self.precio)

    def __str__(self):
        return '%s. %s , %s' %(self.id_paquete,self.nombre, self.lugar)

class Compras(models.Model):
    id_compra = models.CharField(primary_key=True,max_length=50)
    nombre_usuario = models.CharField(max_length=30)
    apellido_usuario = models.CharField(max_length=40)
    nombre_paypal = models.CharField(max_length= 30)
    apellido_paypal = models.CharField(max_length=40)
    correo_cliente = models.EmailField(max_length=100)
    paquete = models.ForeignKey(to=Paquetes, on_delete = models.SET_NULL, null= True)
    n_personas = models.CharField(max_length=10)
    fecha_paquete = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    codigo_estado = models.CharField(max_length=100)
    total_de_compra = models.DecimalField(max_digits=10,decimal_places=2, null = True)

    def __str__(self):
        return self.nombre_usuario        