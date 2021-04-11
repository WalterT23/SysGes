from django.shortcuts import render
from .models import Configuracion
# Create your views here.

def configuracion_view(request):
    #le decimos a django que importe todos los objetos de la clase configuracion
    configuracion = configuracion.objects.all()
    return render(request,"configuracion/configuracion_tpl.html",{'configuracion':configuracion})

