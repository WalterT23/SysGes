from django.db import models
from desarrollo.models import *

# Create your models here.

class Configuracion(models.Model):
    titulo= models.CharField(max_length=200)
    contenido= models.CharField(max_length=200)
    code_url = models.CharField(max_length=200)
    #upload_to es para crear una subcarpeta en medias
    imagen= models.ImageField(upload_to='configuracion')
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name='Modulo Gestion de Configuracion'
        verbose_name_plural='Modulo Gestion de Configuracion'
    
    def __str__(self):
        return self.titulo


class lineaBase(models.Model):
    titulo= models.CharField(max_length=200)
    #tareas= models.ManyToManyField(Tareas)
    tarea_proy= models.ManyToManyField(asignarTareas)
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)
    
    class Meta:
        verbose_name='linea base'
        verbose_name_plural='lineas bases'
    
    def __str__(self):
        return self.titulo