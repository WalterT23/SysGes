from django.contrib import admin
from .models import Desarrollo,Proyectos,Tareas,asignarTareas
# Register your models here.


#Dentro del parentesis va el nombre de la clase que se creo en models

#para agregar los campos en modo lectura
class DesarrolloAdmin(admin.ModelAdmin):
    readonly_fields=('create','updated')

class ProyectosAdmin(admin.ModelAdmin):
    readonly_fields=('create','updated')

class TareasAdmin(admin.ModelAdmin):
    readonly_fields=('create','updated')

class asignarTareasAdmin(admin.ModelAdmin):
    readonly_fields=('create','updated')

admin.site.register(Desarrollo, DesarrolloAdmin)
admin.site.register(Proyectos, ProyectosAdmin)
admin.site.register(Tareas, TareasAdmin)
admin.site.register(asignarTareas, asignarTareasAdmin)
