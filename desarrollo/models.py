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
        verbose_name='desarrollo'
        verbose_name_plural='desarrollos'
    
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
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)
    encargado= models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
    
    def __str__(self):
        return self.titulo

class Tareas(models.Model):
    titulo= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50)
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
    tareasProy= models.ManyToManyField(Proyectos, through='proyecto_tareas')





    class Meta:
        verbose_name='tarea'
        verbose_name_plural='tareas'
    
    def __str__(self):
        return self.titulo

class proyecto_tareas(models.Model):
    proyectos= models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    tareas= models.ForeignKey(Tareas, on_delete=models.CASCADE)
    encargado= models.ForeignKey(User, on_delete=models.CASCADE)
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)
    descripcion= models.CharField(max_length=50)
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

    class Meta:
        verbose_name='Tarea_por_Proy'
        verbose_name_plural='Tareas_por_Proy'

    def __str__(self):
        return self.descripcion



class Dependencias(models.Model):
    descripcion = models.CharField(max_length=50)
    proy_tarea_padre = models.ForeignKey(proyecto_tareas, on_delete=models.CASCADE, related_name='proy_tarea_padre_id')
    proy_tarea_hijo = models.ForeignKey(proyecto_tareas, on_delete=models.CASCADE, related_name='proy_tarea_hijo_id')
    nivel_herencia = models.IntegerField(default=1)
    orden_ejecucion = models.IntegerField(default=1)
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)
    estados_choices = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    estado = models.CharField(
        max_length=50,
        choices=estados_choices,
        default='I',
    )

    class Meta:
        verbose_name='dependencia'
        verbose_name_plural='dependencias'
    
    def __str__(self):
        return self.descripcion
