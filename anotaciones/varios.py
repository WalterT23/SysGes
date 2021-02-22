python manage.py runserver = es para arrancar (ejecutar)el servidor de pruebas (no admite multiples peticiones simultaneas, ni cargas de trabajo pesadas).
python manage.py migrate = es para que el proyecto se encuentre en funcuionamiento

#para crear proyecto ---> 
django-admin startproject nombreProyecto 

#Para crear aplicaciones ---> 
python manage.py startapp nombreApp
python manage.py startapp ProyectoWebApp
#EJEMPLO ----> C:\jess\proyectosDjango\TiendaOnline>python manage.py startapp gestionPedidos

#para cargar los cambios en la base de datos --->
python manage.py makemigrations 

python manage.py migrate

#generar codigo sql
python manage.py sqlmigrate gestionPedidos

#---------PARA IMPACTAR EN LA BASE DE datos
#decirle a nuestro proyecto que tenemos una app nueva en settings.py en installed_apps
python manage.py check nombreApp #para comprobar que todo esta bien en la app --> python manage.py check nombreApp
1- python manage.py makemigrations --->para crear la bd
2- python manage.py sqlmigrate gestionPedidos 0001 --->para ver cuales son los comandos sql que se van a ejecutar
3- python manage.py migrate ----> aplicar la migracion



#-------para hacer insert, update y delete a la base de datos:
1- abrir el shell ----> python manage.py shell
2- importar el modelo sobre el que vamos a trabajar---> from nombreApp.models import nombreClase
>>> from gestionPedidos.models import Articulos
3- Ejemplo de insert, se crea un objeto de la clase con la que vamos a trabajar, y cargamos los valores
>>> art=Articulos(nombre='mesa',seccion='decoracion',precio=90,cantidad=5) 
4- guardar los cambios
>>> art.save()
TAMBIN SE PUEDE INSERTAR USANDO EL METODO CREATE
>>> art3=Articulos.objects.create(nombre='taladro',seccion='ferreteria',precio=65,cantidad=20)

#--------- COMO EDITAR -- update
1- art.precio=95
2- art.save()

#--------- COMO ELIMINAR
1- creamos una variable donde guardar la tupla a ser eliminada colocando la condicion del where en el parentesis ----> art5=Articulos.objects.get(id=6)
2- art5.delete()



#------PARA REALIZAR UN SELECT
1-utilizar una variable con el nombre que queremos y almacenar en ella el resultado de una consulta
Lista=Articulos.objects.all()
2- Ejecutar la variable ----> Lista

#----PARA VER LA INSTRUCCION SELECT
3- Lista.query.__str__()

#----LIBRERIA PARA PODER CONECTAR CON POSTGRES
pip install psycopg2

Articulos.objects.filter(seccion='herramientas',precio='1500') ---> filteer se usa cuando se quiere establecer una clausula del tipo where desde django)

__str__() -----> transforma los objetos en una cadena de caracteres


------VALORES DENTRO DEL SHELL <=>
precio__gte=100 ----> asi decimos que precio es > (MAYOR) al nro 100 cuando se USA en el shell  
precio__lte=100 ----> asi decimos que precio es < (MENOR) al nro 100 cuando se USA en el shell  

-------FUNCION PARA RANGOS
precio__range(10,150) ---> cuando se quire decir un valor entre un cierto rango

Articulos.objects.filter(precio__gte=50) --->mayor o igual
Articulos.objects.filter(precio__gte=50).order_by(precio)----->para ordenar el resultado de menor a mayor
Articulos.objects.filter(precio__gte=50).order_by(-precio)----->para ordenar el resultado de mayor a menor


------CREAR SUPERUSUARIO
python manage.py createsuperuser


#----para EJECUTAR EL servidor
python manage.py runserver


#####---------PARA CERRAR EL runserver
CTRL + C


# PARA UTILIZAR LA API PARA CORREOS
1-Crear archivo forms.py
    1.1 Crear clases por cada formulario que queremos crear

>>> from gestionPedidos.forms import FormularioContacto
>>> miFormulario=FormularioContacto()

#para etiquetas del tipo tabla
>>> print(miFormulario)

#formato  para etiquetas del tipo parrafo
>>> print(miFormulario.as_p())
#formato para etiquetas del tipo lista
>>> print(miFormulario.as_ul())

#el metodo is_valid() dentro del forms
>>> miFormulario.is_valid()
"""Nos permite saber si el formulario a pasado la validacion devolviendo true en caso de ser correcto o false si no.
si devuelve true podemos utilizar la propiedad"""
>>> miFormulario.cleaned_data  
cleaned_data = nos permite obtener la informacion del formulario que han sido enviados
miFormulario=FormularioContacto({'asunto':'prueba','email':'jdprincesita@gmial.com','mensaje':'mensaje de prueba'})