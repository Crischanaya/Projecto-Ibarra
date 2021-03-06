"""SierraTours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from SierraWeb import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('barrancas/', views.barrancas, name='barrancas'),
    path('contacto/', views.contacto, name='contacto'),
    path('creel/', views.creel, name='creel'),
    path('huapoca/', views.huapoca, name='huapoca'),
    path('home/',views.home, name="home"),
    path('', views.index, name= 'index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('nosotros/',views.nosotros,name= 'nosotros'),
    path('recowata/', views.recowata, name='recowata'),
    path('registro/', views.registro, name="registro"),
    path('guardar/', views.add_registro, name="agregarUsuario"),
    path('pasarela/', views.pasarela),
    path('pago/', views.pago, name= "pago"),
]
