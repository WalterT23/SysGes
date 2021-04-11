from django.db import models

# Create your models here.

class Configuracion(models.Model):
    titulo= models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    #upload_to es para crear una subcarpeta en medias
    imagen= models.ImageField(upload_to='configuracion')
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name='configuracion'
        verbose_name_plural='configuraciones'
    
    def __str__(self):
        return self.titulo