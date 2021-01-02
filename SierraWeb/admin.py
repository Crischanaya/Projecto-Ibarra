from django.contrib import admin

# Register your models here.

from SierraWeb.models import UserPaquete, Usuarios, Paquetes

class UsuariosAdmin(admin.ModelAdmin):
    list_display=("id_usuario", "nombre_usuario", "apellido", "correo", "password")
    search_fields=("nombre_usuario","apellido")

class PaquetesAdmin(admin.ModelAdmin):
    list_display=("id_paquete", "nombre", "lugar", "precio")
    search_fields=("nombre", "lugar", "precio")

admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(UserPaquete)
admin.site.register(Paquetes, PaquetesAdmin)