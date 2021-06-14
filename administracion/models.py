from django.db import models
from django.contrib.auth.models import User
from desarrollo.models import Proyectos
# Create your models here.
class Administracion(models.Model):
    titulo= models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    #upload_to es para crear una subcarpeta en medias
    imagen= models.ImageField(upload_to='administracion')
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)
    code_url = models.CharField(max_length=200)

    class Meta:
        verbose_name='Modulo de Administracion'
        verbose_name_plural='Modulos de Administracion'
    
    def __str__(self):
        return self.titulo


class Rol(models.Model):
    titulo= models.CharField(max_length=50)
    descripcion= models.TextField(max_length=50)
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)
    #DEFINIMOS LOS ESTADOS
    estados_choices = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    estado = models.CharField(
        max_length=50,
        choices=estados_choices,
        default='A',
    )
    
    class Meta:
        verbose_name='Rol'
        verbose_name_plural='Roles'
    
    def __str__(self):
        return self.titulo


class Permisos(models.Model):
    tipo_choices = (
        ('C', 'Crear'),
        ('R', 'Leer'),
        ('U', 'Editar'),
        ('D', 'Borrar'),
    )
    tipo = models.CharField(
        max_length=50,
        choices=tipo_choices,
        default='R',
    )
    descripcion= models.TextField(max_length=100)
    #DEFINIMOS LOS ESTADOS
    estados_choices = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    estado = models.CharField(
        max_length=50,
        choices=estados_choices,
        default='A',
    )
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)
    
    class Meta:
        verbose_name='Permiso'
        verbose_name_plural='Permisos'
    
    
    def __str__(self):
        return f"{self.tipo}-{self.descripcion}"
    
    
    

class asignarProyecto(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ManyToManyField(Permisos)
       #DEFINIMOS LOS ESTADOS
    estados_choices = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    estado = models.CharField(
        max_length=50,
        choices=estados_choices,
        default='A',
    )
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)

    
    class Meta:
        verbose_name='- Asignar Proyecto'
        verbose_name_plural='Asignar Proyectos'
        ordering = ["-create"]  # <===== ES PARA ORDENAR LOS REGISTROS POR ESTE CAMPO
    
    def __str__(self):
        return f"{self.proyecto}-{self.usuario}"
    
