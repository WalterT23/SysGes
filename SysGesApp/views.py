from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from SysGes import settings

# Create your views here.

def home_view(request):
    # return HttpResponse("Home") #solo muestra texto
    #para mostrar lo que esta en mi template
    return render(request,"SysGesApp/home_tpl.html")


"""
def configuracion_view(request):
    return render(request,"SysGesApp/configuracion_tpl.html")
"""


########### GESTIONAR USUARIO
#para generar un nuevo usuario
def nuevo_usuario(request):
    if request.method=='POST':
        formulario= UserCreationForm(request.POST)


        if formulario.is_valid:
           
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario=UserCreationForm()
        #GUARDAMOS LOS MENSAJES DE VALIDACION
        val_username =  formulario.fields['username'].help_text 
        val_pass1 = formulario.fields['password1'].help_text 
        val_pass2 = formulario.fields['password2'].help_text

        #LIMPIAMOS PARA QUE NO NOS MUESTRE LOS MENSAJES DE VALIDACION
        formulario.fields['username'].help_text = None
        formulario.fields['password1'].help_text = None
        formulario.fields['password2'].help_text = None
    return render(request,"SysGesApp/usuario/nuevousuario.html",{'formulario':formulario})


def ingresar(request):
    #agregamos este primer if para que no nos vuelva a pedir que nos logueemos al ir a privado si es que ya lo hicimos
    #if not request.user.is_anonymous():
    #   return HttpResponseRedirect('SysGesApp/usuario/privado')
    #Notar que existe una condicional que menciona “is_active”, 
    # eso nos indica que el usuario puede que exista en el sistema, 
    # pero también debe estar activo para poder ingresar.
    if request.method =='POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
                usuario= request.POST['username']
                clave = request.POST['password']
                acceso = authenticate(username=usuario, password=clave)
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        return HttpResponseRedirect('/privado')
                    else:
                        return render(request,"SysGesApp/usuario/noactivo.html",{'formulario':formulario})
                else:
                    return render(request,"SysGesApp/usuario/nousuario.html",{'formulario':formulario})
    else:
        formulario=AuthenticationForm()
    return render(request,"SysGesApp/usuario/ingresar.html",{'formulario':formulario})


@login_required(login_url='/ingresar')#esto se coloca para que no se pueda acceder a esta area sin haberce logueado, se debe poner encima de la vista siempre
def privado(request):
    usuario= request.user
    return render(request,"SysGesApp/usuario/privado.html",{'usuario':usuario})

#view para cerrar la sesion
@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')