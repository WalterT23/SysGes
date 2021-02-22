"""SysGes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


    Ejemplos:
Vistas de funciones
    1. Agregar una importación: desde vistas de importación my_app
    2. Agregue una URL a urlpatterns: ruta ('', views.home, name = 'home')
Vistas basadas en clases
    1. Agregar una importación: de other_app.views import Home
    2. Agregue una URL a urlpatterns: ruta ('', Home.as_view (), name = 'home')
Incluyendo otra URLconf
    1. Importe la función include (): desde django.urls import include, path
    2. Agregue una URL a urlpatterns: ruta ('blog /', include ('blog.urls'))
"""


#ARCHIVO URL DEL PROYECTO EN TOTAL
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    #aqui se enlaza con la pag de urls de la aplicacion
    path('', include('SysGesApp.urls')),
    path('administracion/', include('administracion.urls')),


       
#   path('SysGesApp/', include('SysGesApp.urls')),        

]


