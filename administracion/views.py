from django.shortcuts import render
from .models import Administracion
# Create your views here.

def administracion_view(request):
    #le decimos a django que importe todos los objetos de la clase Administracion
    administracion = Administracion.objects.all()
    return render(request,"administracion/administracion_tpl.html",{'administracion':administracion})

