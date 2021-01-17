from django.contrib import admin

# Register your models here.

from SierraWeb.models import Usuarios, Paquetes, Compras

class UsuariosAdmin(admin.ModelAdmin):
    list_display=("id_usuario", "nombre_usuario", "apellido", "correo", "password")
    search_fields=("nombre_usuario","apellido")

class PaquetesAdmin(admin.ModelAdmin):
    list_display=("id_paquete", "nombre", "lugar", "precio","fecha")
    search_fields=("nombre", "lugar", "precio","fecha")

class ComprasAdmin(admin.ModelAdmin):
    list_display = ("nombre_usuario", "apellido_usuario","correo_cliente","paquete","status","total_de_compra")    
    search_fields =("nombre_usuario", "apellido_usuario")

admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Paquetes, PaquetesAdmin)
admin.site.register(Compras,ComprasAdmin)