from django.shortcuts import render

def barrancas(request):
    return render(request, "barrancas.html")

def contacto(request):
    return render(request, "contacto.html")

def creel(request):
    return render(request, "creel.html")

def huapoca(request):
    return render(request, "huapoca.html")

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def nosotros(request):
    return render(request, "nosotros.html")

def recowata(request):
    return render(request, "recowata.html")

def registro(request):
    return render(request, "registro.html")