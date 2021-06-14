from django.shortcuts import render
from .models import Configuracion
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/ingresar')
def configuracion_view(request):
    #le decimos a django que importe todos los objetos de la clase configuracion
    configuracion = Configuracion.objects.all()
    return render(request,"configuracion/configuracion_tpl.html",{'configuracion':configuracion})




