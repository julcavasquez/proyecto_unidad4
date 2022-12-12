from django.db import models

# Creando mi modelo usuario

class Usuario(models.Model):
    nombre = models.CharField(max_length=25)
    user_name = models.CharField(max_length=15)
    password = models.CharField(max_length=150)

    class Meta:
        db_table='usuario'

 

class Proyecto(models.Model):
    foto = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    tags = models.CharField(max_length=50)
    url_repo = models.CharField(max_length=150)
    idusuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True)

    class Meta:
        db_table='proyecto'
