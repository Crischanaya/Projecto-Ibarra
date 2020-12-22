from django.shortcuts import render

# Create your views here.
def barrancas(request):
    return render(request, "SierraWeb/barrancas.html")

def contacto(request):
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

def recowata(request):
    return render(request, "SierraWeb/recowata.html")

def registro(request):
    return render(request, "SierraWeb/registro.html")