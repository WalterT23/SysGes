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



def configuracion_view(request):
    return render(request,"SysGesApp/configuracion_tpl.html")


def desarrollo_view(request):
    #nombre de la carpeta dentro de la carpeta template/nombre archivo html
    return render(request,"SysGesApp/desarrollo_tpl.html")


