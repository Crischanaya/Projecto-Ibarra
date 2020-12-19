
from django.contrib import admin
from django.urls import path
from SierraTours.Directorioweb import barrancas, contacto, creel, huapoca, index, login, nosotros, recowata, registro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('barrancas/', barrancas),
    path('contacto/', contacto),
    path('creel/', creel),
    path('huapoca/', huapoca),
    path('index/', index),
    path('login/', login),
    path('nosotros/', nosotros),
    path('recowata/', recowata),
    path('registro/', registro),
]
