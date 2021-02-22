from django.db import models


# Create your models here.
class Administracion(models.Model):
    titulo= models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    #upload_to es para crear una subcarpeta en medias
    imagen= models.ImageField(upload_to='administracion')
    create= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name='administracion'
        verbose_name_plural='administraciones'
    
    def __str__(self):
        return self.titulo