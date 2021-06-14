from django.contrib import admin
from .models import Configuracion,lineaBase
# Register your models here.


#Dentro del parentesis va el nombre de la clase que se creo en models

#para agregar los campos en modo lectura
class ConfiguracionAdmin(admin.ModelAdmin):
    readonly_fields=('create','updated')
    
class lineaBaseAdmin(admin.ModelAdmin):
    readonly_fields=('create','updated')
    
admin.site.register(Configuracion, ConfiguracionAdmin)
admin.site.register(lineaBase, lineaBaseAdmin)