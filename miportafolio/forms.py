from django import forms
from miportafolio.models import Usuario
class LoginUser(forms.Form):
    attrs_usu = {
        "type": "name",
        "id":"nom_usuario" ,
        "name":"nom_usuario" ,
        "placeholder":"Nom. Usuario",
        "required":""
    }
    attrs_pass = {
        "type": "password",
        "id":"password" ,
        "name":"password" ,
        "placeholder":"Contraseña",
        "required":""
    }
    user_name = forms.CharField(max_length=15,widget=forms.TextInput(attrs=attrs_usu),label=False)
    password = forms.CharField(max_length=15,widget=forms.TextInput(attrs=attrs_pass),label=False)

class RegistrarUser(forms.Form):
    attrs_nya = {
        "type": "name",
        "id":"nombres" ,
        "name":"nombre" ,
        "placeholder":"Nombres y Apellidos",
        "autocomplete":"on",
        "required":""
    }
    attrs_user = {
        "type": "name",
        "id":"nom_usuario" ,
        "name":"user_name" ,
        "placeholder":"Nombre Usuario",
        "autocomplete":"on",
        "required":""
    }
    attrs_pass = {
        "type": "password",
        "id":"password" ,
        "name":"password" ,
        "placeholder":"Contraseña",
        "required":""
    }
    nombre = forms.CharField(max_length=15,widget=forms.TextInput(attrs=attrs_nya),label=False)
    user_name = forms.CharField(max_length=15,widget=forms.TextInput(attrs=attrs_user),label=False)
    password = forms.CharField(max_length=15,widget=forms.TextInput(attrs=attrs_pass),label=False)

    