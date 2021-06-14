from administracion.forms import RolForm
from django.shortcuts import render, redirect
from .models import Administracion
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/ingresar')
def administracion_view(request):
    #le decimos a django que importe todos los objetos de la clase Administracion
    administracionForm = Administracion.objects.all()
    return render(request,"administracion/administracion_tpl.html",{'administracionForm':administracionForm})

@login_required(login_url='/ingresar')
def rol_view(request):
    #vamos a leer si el request es un post
    if request.method == 'POST':
        rolesForm = RolForm(request.POST)
        #si lo que se recibe es un post, vamos a preguntar si los datos que se ingresaron son validos, en caso de ser asi, se van a guardar los valores
        if rolesForm.is_valid():
            rolesForm.save()
        return redirect('administracion:rol')
    else:
        rolesForm = RolForm()
    return render(request,"administracion/roles_tpl.html",{'rolesForm':rolesForm})
