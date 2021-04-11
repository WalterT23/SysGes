from django.shortcuts import render, redirect
from .models import Desarrollo
from .forms import FormularioCrearProyecto

# Create your views here.

def desarrollo_view(request):
    #le decimos a django que importe todos los objetos de la clase desarrollo
    desarrollo = Desarrollo.objects.all()
    return render(request,"desarrollo/desarrollo_tpl.html",{'desarrollo':desarrollo})

#para generar un nuevo proyecto
def crear_proyecto(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_crear_proy = FormularioCrearProyecto(data= request.POST)
        # check whether it's valid:
        if form_crear_proy.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            titulo= request.POST.get("titulo")
            descripcion= request.POST.get("descripcion")
            fecha_inicio=request.POST.get("fecha_inicio")
            fecha_fin=request.POST.get("fecha_fin")

            #form_crear_proy.save()
        return redirect("/desarrollo/proyecto/nuevo/?valido")

    # if a GET (or any other method) we'll create a blank form
    else:
        form_crear_proy = FormularioCrearProyecto()

    return render(request,"desarrollo/proyecto/crear_proyecto_tpl.html",{'form_crear_proy':form_crear_proy})