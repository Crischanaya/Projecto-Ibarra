from django.http import HttpRequest
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from SierraWeb.models import Usuarios

# Create your views here.
def barrancas(request):
    return render(request, "SierraWeb/barrancas.html")

def contacto(request):
    if request.method=="POST":
       
        subject=request.POST["asunto"] 

        if request.POST["contacto"] == "telefono":
            contactar = "telefono"
        else:
            contactar = "correo"      

        message= "Nombre: "+ request.POST["nombre"]  +"\nMensaje:"+ request.POST["mensaje"] + "\nCorreo: " + request.POST["correo"] + "\nTeléfono: " + request.POST["telefono"] + "\nContactar: " + contactar + "\nFecha a Contactar: " + request.POST["fecha"] + "\nHora a Contactar: " + request.POST["hora"]

        email_from=settings.EMAIL_HOST_USER

        recipient_list=["agenciasierratours@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

    return render(request, "SierraWeb/contacto.html")

def creel(request):
    return render(request, "SierraWeb/creel.html")

def huapoca(request):
    return render(request, "SierraWeb/huapoca.html")

def index(request):
    return render(request, "SierraWeb/index.html")

def login(request):
    return render(request, "SierraWeb/login.html")

def nosotros(request):
    return render(request, "SierraWeb/nosotros.html")
    
def reservacion(request):
    return render(request, "SierraWeb/reservacion.html")    

def recowata(request):
    return render(request, "SierraWeb/recowata.html")

def registro(request):
  
    return render(request, "SierraWeb/registro.html")

def pasarela(request):
    return render(request, "SierraWeb/pasarela.html")    

def add_registro(request):
    print("ENTRO AL GUARDADO")
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    correo = request.POST["correo"]
    password = request.POST["password"]
    usuarios = Usuarios(nombre_usuario=nombre,apellido=apellido,correo=correo,password=password)
    usuarios.save()
    if usuarios != None:
        respuesta = "completed";
        print(usuarios)
    else:
        respuesta = "error";

    return render(request, "SierraWeb/registro.html",{"respuesta":respuesta})    
