from django.contrib import admin
from .models import Administracion,Rol,Permisos,asignarProyecto
# Register your models here.


#Dentro del parentesis va el nombre de la clase que se creo en models

#para agregar los campos en modo lectura
class AdministracionAdmin(admin.ModelAdmin):
    readonly_fields=('create','updated')
    model = Administracion
    
def get_actions(self, request):
    actions = super(AdministracionAdmin, self).get_actions(request) # Obtenemos todas las acciones de este modelo
    print(actions)
    del actions['delete_selected'] # Deshabilitamos la opción de borrar
    return actions

class AdminRol(admin.ModelAdmin):
    readonly_fields=('create','updated')

class AdminPermisos(admin.ModelAdmin):
    readonly_fields=('create','updated')

class AdminasignarProyecto(admin.ModelAdmin):
    readonly_fields=('create','updated')

admin.site.register(Administracion, AdministracionAdmin)
admin.site.register(Rol, AdminRol)
admin.site.register(Permisos, AdminPermisos)
admin.site.register(asignarProyecto, AdminasignarProyecto)


