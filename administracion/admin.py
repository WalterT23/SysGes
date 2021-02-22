from django.contrib import admin
from .models import Administracion
# Register your models here.


#Dentro del parentesis va el nombre de la clase que se creo en models

#para agregar los campos en modo lectura
class AdministracionAdmin(admin.ModelAdmin):
    readonly_fields=('create','updated')



admin.site.register(Administracion, AdministracionAdmin)



