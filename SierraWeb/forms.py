from django import forms

from SierraWeb.models import Usuarios


class FormularioRegistroUser(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'