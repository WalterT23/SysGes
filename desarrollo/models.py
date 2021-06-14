from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Desarrollo(models.Model):
    titulo= models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    #upload_to es para crear una subcarpeta en medias
    imagen= models.ImageField(upload_to='desarrollo')
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)
    code_url = models.CharField(max_length=250)

    class Meta:
        verbose_name='Modulo de desarrollo'
        verbose_name_plural='Modulos de desarrollo'
    
    def __str__(self):
        return self.titulo



class Tareas(models.Model):
    titulo= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50)
    proy_tarea_padre = models.ForeignKey('self', on_delete=models.CASCADE, related_name='id_tarea_padre', null=True, blank=True)
    nivel_herencia = models.IntegerField(default=0)
    orden_ejecucion = models.IntegerField(default=1)
    #DEFINIMOS LOS ESTADOS DE LAS TAREAS 
    estados_choices = (
        ('I', 'Iniciado'),
        ('P', 'Pendiente'),
        ('F', 'Finalizado'),
    )
    estado = models.CharField(
        max_length=50,
        choices=estados_choices,
        default='P',
    )
    fecha_inicio=models.DateTimeField()
    fecha_fin=models.DateTimeField()
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)

    
    class Meta:
        verbose_name='tarea'
        verbose_name_plural='tareas'
    
    def __str__(self):
        return self.titulo


class Proyectos(models.Model):
    titulo= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50)
    #DEFINIMOS LOS ESTADOS DE LOS PROYECTOS
    estados_choices = (
        ('I', 'Iniciado'),
        ('P', 'Pendiente'),
        ('F', 'Finalizado'),
    )
    estado = models.CharField(
        max_length=50,
        choices=estados_choices,
        default='P',
    )
    fecha_inicio=models.DateTimeField()
    fecha_fin=models.DateTimeField()
    tareasProy= models.ManyToManyField(Tareas, through='asignarTareas')
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)
    
    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
    
    def __str__(self):
        return self.titulo


class asignarTareas(models.Model):
    proyectos= models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    tareas= models.ForeignKey(Tareas, on_delete=models.CASCADE)
    encargado= models.ForeignKey(User, on_delete=models.CASCADE)
    titulo= models.CharField(max_length=50)
    version= models.CharField(max_length=50, default="1")   
    prioridad_choices = (
        ('A', 'Alta'),
        ('B', 'Baja'),
        ('M', 'Media'),
    )
    prioridad = models.CharField(
        max_length=50,
        choices=prioridad_choices,
        default='B',
    )
    observacion= models.CharField(max_length=500, default="")
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)
    
    class Meta:
        verbose_name='Tarea por proyecto'
        verbose_name_plural='Tareas por proyectos'

    def __str__(self):
        return self.titulo
