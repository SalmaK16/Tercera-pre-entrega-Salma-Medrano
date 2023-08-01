from django.db import models

# Create your models here.
class Reseña(models.Model):
# los atributos de clase (son las columnas de la tabla)
    nombre_libro = models.CharField(max_length=64)
    autora = models.CharField(max_length=256)
    comentario = models.CharField(max_length=600)


class Novedades(models.Model):
    autora = models.CharField(max_length=256)
    nombre_libro = models.CharField(max_length=256)
    fecha_publicacion = models.DateField(null=True)
    genero = models.CharField(max_length=50)
    

class Top10(models.Model):
    autora = models.CharField(max_length=256)
    nombre_libro = models.CharField(max_length=256)
    genero = models.CharField(max_length=50)
    puntuacion = models.IntegerField()


class Nuevas_Autoras(models.Model):
    nombre = models.CharField(max_length=256)
    nacionalidad = models.CharField(max_length=50)
    